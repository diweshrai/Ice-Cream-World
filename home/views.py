from typing import ContextManager
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm






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
 

def soft(request):
    return render(request, 'soft.html') 



def organic(request):
    return render(request, 'organic.html') 

def hard(request):
    return render(request, 'hard.html') 

def nosugar(request):
    return render(request, 'nosugar.html') 

def french(request):
    return render(request, 'french.html') 

def light(request):
    return render(request, 'light.html')  


def sign(request):
    return render(request, 'sign.html')        


def register(request):
    return render(request, 'register.html') 


