from django.db import models

# Create your models here.
class news(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
