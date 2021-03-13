from django.contrib import admin
from .models import Post, Counsel
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = (
        'title',
        'user',
    )


@admin.register(Counsel)
class CounselAdmin(SummernoteModelAdmin):
    list_display = (
        'title',
        'name',
    )