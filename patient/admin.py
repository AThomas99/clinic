from django.contrib import admin
from .models import Patient, Vital

admin.site.register(Patient)
admin.site.register(Vital)