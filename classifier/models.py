from django.db import models

# Create your models here.

class Images(models.Model):
    imageid = models.AutoField(primary_key=True)
    url = models.TextField(unique=True)
    label = models.TextField(default='')


