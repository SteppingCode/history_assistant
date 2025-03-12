from django.db import models

class WW2Event(models.Model):
    date = models.DateField()
    description = models.TextField()
    category = models.CharField(max_length=100)

class TatneftHistory(models.Model):
    date = models.DateField()
    event = models.CharField(max_length=100)
    description = models.TextField()