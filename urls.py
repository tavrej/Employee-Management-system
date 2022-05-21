from django.urls import path
from CMSApp.views import *
from django.contrib import admin  
from django.urls import path 
  


#BASE URL =http://127.0.0.1:8000/cms/

urlpatterns = [
    path('result/',view_result),
    path('factorial/',view_factorial),
    path('LCM/',view_LCM),
    path('customer/',cms_view), 
    path('employee/',ems_view),
    path('table/',view_table) 
] 
    

