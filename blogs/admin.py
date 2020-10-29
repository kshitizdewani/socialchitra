from django.contrib import admin
from blogs.models import Blog
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)


admin.site.register(Blog,BlogAdmin)
