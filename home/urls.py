from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
     path("about", views.about, name='about'),
    path("howtoreach", views.howtoreach, name='howtoreach'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'), 
    path("events", views.all_events, name='list-events'),
    
    
    

]