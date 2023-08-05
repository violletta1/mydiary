from django.contrib import admin

from django.contrib import admin
from Beauty.diary.models import Post,Note


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title','user', 'created_at', 'updated_at')
    search_fields = ('title','created_at',)
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)

@admin.register(Note)
class NotesAdmin(admin.ModelAdmin):
    list_display = ('user','title', 'created_at','updated_at')
    search_fields = ('title',)
    list_filter = ('title',)
    ordering = ('-updated_at',)
