from django.db import models

# Create your models here.
class Deliver(models.Model):
    deliver_id = models.CharField(max_length=8,primary_key=True)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()