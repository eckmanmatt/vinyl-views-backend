from django.db import models

# Create your models here.
class Record(models.Model):
    title = models.CharField(max_length=32)
    artist = models.CharField(max_length=32)
    year = models.IntegerField()
    cover = models.CharField(max_length=32)
