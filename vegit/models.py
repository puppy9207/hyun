from django.db import models

class Vegit(models.Model):
    vegit_date = models.CharField(max_length=40)
    vegit_pred = models.FloatField()

# Create your models here.
