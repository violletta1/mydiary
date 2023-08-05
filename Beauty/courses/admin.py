from django.contrib import admin

# Register your models here.
from django.contrib import admin
from Beauty.courses.models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ( 'user','title', 'category', 'created_at', 'updated_at')
    search_fields = ('title','created_at',)
    list_filter = ('created_at', 'updated_at')
