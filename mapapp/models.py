# models.py

from django.db import models

class SelectedDistrict(models.Model):
    # A field to store the district name (e.g., "Tverskoy")
    name = models.CharField(max_length=255)

    # A string representation of the model (to make it easier to debug)
    def __str__(self):
        return self.name
