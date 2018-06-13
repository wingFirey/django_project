# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.
from django.views.generic import TemplateView
from .models import Patient
from django.http import HttpResponse,Http404,HttpResponseRedirect
from webApp.forms import PatientForm
from django.contrib.auth.models import User

class PatientUpdate(UpdateView):
   model = Patient
   fields = ['patient_name','patient_ID','patient_age','patient_issue','other_details',]

def edit(request):
   if not request.user.is_authenticated():
      return render(request,'error.html',{})
   else:
      if request.method == "POST":
         id = request.POST['edit_query']
         return redirect('/homepage/%s/edit' % id)
      else:
         return render(request,'edit.html',{})

def detail(request):
   if not request.user.is_authenticated():
      return render(request,'error.html',{})
   else:
      form = PatientForm()
      patients = Patient.objects.all()
      print(patients)
      args = {'form':form,'patients':patients}
      return render(request,'details.html',args)
  

def index(request):
   return render(request,'homepage.html',{})

def show(request):
   return render(request,'submitted.html',{})

def ivh(request):
   return render(request,'view.html',{})   

def finalview(request):
   return render(request,'finalview.html',{})



def final_edit(request,id = None):
   if not request.user.is_authenticated():
      return render(request,'error.html',{})
   else:
      instance = get_object_or_404(Patient,pk =id)
         
      form = PatientForm(request.POST or None, request.FILES or None,instance = instance)

      print "these are the errors"
      print form.errors
      if form.is_valid():   
         print "form is valid"
         instance = form.save(commit=False) 
         instance.user = request.user      
         instance.save()
         return render(request,'updated.html',{})      
      args = {'instance':instance,'form':form,}
      return render(request,'final_edit.html',args)


def view(request):
   if not request.user.is_authenticated():
      return render(request,'error.html',{})
   else:
      form = PatientForm()
      patients = Patient.objects.all()
      temp=0
      if request.method =='POST':
         id = request.POST['search_query']
         temp=id
      patient=0
      for i in patients:
         if i.patient_ID==temp:
            patient =i;
            print i.patient_name
      print ('hi there')
      args = {'form':form,'patient':patient}
      return render(request,'finalview.html',args)
  

def register(request):
   if not request.user.is_authenticated():
      return render(request,'error.html',{})

   if request.method == 'POST':
      form = PatientForm(request.POST or None, request.FILES or None)
      print request.POST
      if form.is_valid():
         print "form is valid"
         #form.save() 
         post = form.save(commit=False)
         post.user = request.user
         post.save()

         patient_name = form.cleaned_data['patient_name']       
         patient_ID = form.cleaned_data['patient_ID']
         patient_age = form.cleaned_data['patient_age']
         patient_issue = form.cleaned_data['patient_issue']
         other_details = form.cleaned_data['other_details']
         
         form = PatientForm()         
         return redirect('submitted.html')
      args = {'form':form,'patient_name':patient_name,'patient_ID':patient_ID,'patient_age':patient_age,'patient_issue':patient_issue,'other_details':other_details}
      return render(request,'register.html',args)
   else:
      form = PatientForm()
      #patients = Patient.objects.all()
      #print('hey')
     # print(patients)
     # args = {'form':form,'patients':patients}
      return render(request,'register.html',{'form':form})




   
