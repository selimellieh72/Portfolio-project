from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
from .models import blog
class BodyAdmin(SummernoteModelAdmin):
	summernote_fields = 'body'
admin.site.register(blog,BodyAdmin)
