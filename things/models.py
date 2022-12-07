from django.db import models

class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(max_length=120, blank=True)
    quantity = models.PositiveIntegerField(max_length=100)

