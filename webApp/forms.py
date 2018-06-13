from django import forms
from webApp.models import Patient
from django.contrib.auth.models import User

class PatientForm(forms.ModelForm):
   patient_name = forms.CharField(max_length= 20)
   patient_ID = forms.CharField(max_length =20)
   patient_age = forms.CharField(max_length = 5)
   patient_issue = forms.CharField(max_length =30)
   other_details = forms.CharField(max_length =40)
   #patient_file = forms.ImageField(upload_to = 'uploads/')

   class Meta:
      model = Patient
      fields ='__all__'


