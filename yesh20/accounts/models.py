from django.db import models

# Create your models here.
class Details(models.Model):
    name = models.CharField(max_length=30)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    offer = models.BooleanField(default=False)
    price = models.IntegerField()