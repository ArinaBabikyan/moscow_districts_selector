from django.contrib import admin

# Register your models here.
# admin.py
from .models import SelectedDistrict

# Register the model to the admin site
admin.site.register(SelectedDistrict)
