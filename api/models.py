# django imports
from django.db import models


class FibonacciModel(models.Model):
    # Nth number to be given as input to fibonacci series
    number = models.IntegerField(verbose_name='number',null=False, blank=False)
