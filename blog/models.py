from django.db import models
# Create your models here.
class blog(models.Model):
    created = models.DateTimeField()
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/")
    body = models.TextField()
    def __str__(self):
        return self.title
    def showcase(self):
        return self.body[:100]
    def pretty_date(self):
        return self.created.strftime("%B %e %Y")
