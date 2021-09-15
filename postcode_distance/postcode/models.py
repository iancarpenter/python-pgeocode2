from django.db import models

class Postcode(models.Model):
    start_postcode = models.CharField(max_length=4)
    end_postcode = models.CharField(max_length=4)
    result_measurement_unit = models.CharField(max_length=4)