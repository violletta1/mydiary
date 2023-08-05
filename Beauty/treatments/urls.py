from django.urls import path,include
from Beauty.treatments.views import list_treatments, CreateTreatment, edit_treatment, delete_treatment, \
    details_treatment, treatment_search

urlpatterns = [
    path('create_treatment/', CreateTreatment.as_view(), name='create_treatment'),
    path('treatment_search/', treatment_search, name='treatment_search'),
    path('list_treatments/',list_treatments, name='list_treatments'),
    path('details/<int:pk>/', details_treatment, name='treatment_details'),
    path('edit/<int:pk>/', edit_treatment, name='edit_treatment'),
    path('delete/<int:pk>/', delete_treatment, name='delete_treatment')]

