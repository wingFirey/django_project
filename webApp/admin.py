# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Patient

#admin.site.register(Patient)

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
   list_display = ('patient_name','patient_ID','patient_age','patient_issue')


