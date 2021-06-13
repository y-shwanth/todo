from django.db import models

# Create your models here.
class Todo(models.Model):
    added_date = models.DateField()
    text = models.CharField(max_length=200)
    user_name = models.CharField(max_length=20, default='UNKNOWN')