from urllib import request
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from home.models import Grievance
from django.contrib import messages
from .models import Event
from .models import Student


def all_events(request):
    event_list= Event.objects.all()
    return render(request,'events/event_list.html', 
    {'event_list': event_list})


# Create your views here.
def index(request):
    context = {
        "variable1":"Harry is great",
        "variable2":"Rohan is great"
    } 
    return render(request, 'index.html', context)
    # return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html') 

def howtoreach(request):
    return render(request, 'howtoreach.html') 

def services(request):
    return render(request, 'services.html')
 

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')
 