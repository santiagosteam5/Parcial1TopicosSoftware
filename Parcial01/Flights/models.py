from django.db import models


class Flight(models.Model):
    type_options = [('Nacional', 'Nacional'), ('Internacional', 'Internacional')]
    id = models.AutoField(primary_key=True)
    flight_name = models.CharField(max_length=100)
    flight_type = models.CharField(max_length=100, choices=type_options, default='Nacional')
    flight_price = models.FloatField()
