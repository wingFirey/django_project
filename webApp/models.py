from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

# Create your models here.
def upload_location(instance,filename):
   return "%s/%s"  %(instance.pk,filename)
class Patient(models.Model):
   patient_name = models.CharField(max_length= 30, help_text = "Name")
   patient_ID = models.CharField(max_length =20, help_text = 'Patient ID')
   patient_age = models.CharField(max_length= 5, help_text = ' Age')
   patient_issue = models.CharField(max_length = 40, help_text = 'Issue')
   other_details = models.CharField(max_length = 40, help_text = 'Other Details')
   patient_file = models.ImageField(upload_to= upload_location,null=True,blank=True)
   date = models.DateTimeField(auto_now=True)
   
   user = models.ForeignKey(User)
   #sets patient ID as unique primary key to identify all records
   patient_ID.primary_key = True





   def __str__(self):
     return self.patient_ID
