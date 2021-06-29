from django.db import models

# Create your models here.
class Article(models.Model):
    article = models.CharField(max_length=20000)
    xueduan = models.IntegerField()

