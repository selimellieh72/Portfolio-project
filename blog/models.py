from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class blog(models.Model):
    created = models.DateTimeField()
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/")
    body = RichTextUploadingField()
    def __str__(self):
        return self.title
    def showcase(self):
        return self.body[:100]
    def pretty_date(self):
        return self.created.strftime("%B %e %Y")
