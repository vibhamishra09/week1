from django.db import models
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email= models.CharField(max_length=122)
    phone = models.FileField(upload_to="static/media", max_length=100)
    desc = models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.name
# Create your models here.
