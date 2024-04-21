from django.db import models

# Create your models here.

class Calculation(models.Model):
    principle = models.DecimalField(max_digits=10,decimal_places=2)
    rate = models.DecimalField(max_digits=10,decimal_places=2)
    time = models.IntegerField()
    result = models.DecimalField(max_digits=10,decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    