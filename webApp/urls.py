from django.conf.urls import url,include
from . import views
from django.contrib.auth.views import login,logout


urlpatterns =[
  url(r'^$',views.index,name ='index'),
  url(r'^register',views.register, name = 'register'),
  url(r'^submitted',views.show, name = 'submitted'),
  url(r'homepage',views.index,name = 'index'),
  url(r'^view/(?P<user_id>\D+)/',views.view, name ='view'),
  url(r'^view',views.ivh, name ='view'),
  #url(r'edit',views.edit, name = 'edit'),
  url(r'^login',login,{'template_name':'login.html'}),
  url(r'^logout',logout,{'template_name':'logout.html'}),
  url(r'^finalview',views.view, name ='finalview'),
  url(r'^details',views.detail,name = 'detail'),
 # url(r'^(?P<id>\D+)/edit/',views.final_edit,name ='update'),
  url(r'^(?P<id>\w+)/edit/',views.final_edit,name ='update'), 
  url(r'^edit',views.edit,name = "edit"),
  #url(r'^pre_edit',views.PatientUpdate.as_view(),name = 'patient_update'),
 
];
