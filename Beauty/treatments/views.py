from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render,redirect
from django.utils.decorators import method_decorator
from django.views import generic as views
from django.urls import reverse, reverse_lazy
from .models import Treatment
from Beauty.treatments.forms import TreatmentAddForm, TreatmentEditForm
from ..accounts.decorators import is_practitioner_group_user
from ..common.forms import CommentForm
from django.shortcuts import get_object_or_404


def treatment_search(request):
    query = request.GET.get('q')
    if query:
        results = Treatment.objects.filter(title__icontains=query)
    else:
        results = None

    return render(request, 'treatments/treatments_search_results.html', {'results': results})

def list_treatments(request):
    is_practitioner = is_practitioner_group_user(request.user)
    current_user = request.user
    treatments = Treatment.objects.all().order_by('-created_at')
    treatment_creators = {}
    for treatment in treatments:
        treatment_creators[treatment] = treatment.user

    context = {
        'current_user': current_user,
        'treatment_creators': treatment_creators,
        'treatments':treatments,
        'is_practitioner':is_practitioner}
    return render(request, template_name='treatments/treatments_list.html', context=context)


@method_decorator(user_passes_test(is_practitioner_group_user), name='dispatch')
class CreateTreatment(LoginRequiredMixin,views.CreateView):
    model = Treatment
    form_class = TreatmentAddForm
    template_name = 'treatments/treatment_create.html'

    def get_success_url(self):
        return reverse('treatment_details', kwargs={
            'pk': self.object.pk
        })

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)

        form.instance.user = self.request.user
        return form

def details_treatment(request,pk):
    treatment = Treatment.objects.get(pk=pk)
    comment_form = CommentForm()
    user_who_created_it = treatment.user
    user = request.user
    context = {
        'current_user': user,
        'treatment':treatment,
        'comments':treatment.comment_set.all(),
        'comment_form':comment_form,
        'likes':treatment.like_set.count(),
        'user_who_created_it':user_who_created_it,

    }
    return render(
        request,
        'treatments/treatment_details.html',
        context=context
    )

@login_required
def edit_treatment(request,pk):

    treatment = get_object_or_404(Treatment, pk=pk)
    user_who_created_it = treatment.user
    form = TreatmentEditForm(instance=treatment)

    if request.user != treatment.user:
        return redirect('no_access')

    if request.method == "POST":
        form = TreatmentEditForm(request.POST, instance=treatment)
        if form.is_valid():
            form.save()
            return redirect('treatment_details', pk=pk)

    context = {
        "treatment": treatment,
        "form": form,
        'user_who_created_it': user_who_created_it,
    }

    return render(request, 'treatments/edit_treatment.html', context)

def delete_treatment(request,pk):
    treatment = Treatment.objects.filter(pk=pk).get()
    if request.user != treatment.user:
        return redirect('no_access')
    treatment.delete()
    return redirect('list_treatments')
