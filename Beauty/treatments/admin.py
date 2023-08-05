from django.contrib import admin
from Beauty.treatments.models import Treatment
# Register your models here.

@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'created_at', 'updated_at','user')
    search_fields = ('title','created_at',)
    list_filter = ('created_at', 'updated_at')


