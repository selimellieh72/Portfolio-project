from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
from .models import blog
from .models import tag
class BodyAdmin(SummernoteModelAdmin):
	summernote_fields = 'body'

class TagAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}
admin.site.register(tag,TagAdmin)
admin.site.register(blog,BodyAdmin)
