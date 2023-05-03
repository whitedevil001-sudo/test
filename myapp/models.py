from django.db import models
class test (models.Model):
    name=models.CharField(max_length=50)
    id=models.PositiveIntegerField(primary_key=True)
    location=models.CharField(max_length=50)
# Create your models here.
