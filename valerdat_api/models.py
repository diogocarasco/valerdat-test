from django.db import models

class Prod(models.Model):
    ref = models.IntegerField
    zipcode = models.IntegerField
    store = models.CharField(max_length = 100)
    amount = models.FloatField

    def __str__(self):
        return self.task