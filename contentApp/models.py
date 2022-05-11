from django.db import models

# Create your models here.
class Content(models.Model):
    title = models.CharField(max_length=100)
    source = models.CharField(max_length=30)
    topic = models.CharField(max_length=30)
    date = models.DateField()