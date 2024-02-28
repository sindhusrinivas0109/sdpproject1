# Create your views here.
def hello(request):
    return render(request,'hello123.html')
def hello1(request):
    return HttpResponse("<center>Welcome to TTM homepage</center>")

def newhomepage(request):
    return render(request,'newhomepage.html')

def travelpackage(request):
    return render(request,'travelpackage.html')

def carrent(request):
    return render(request,'cars123.html')



from django.http import HttpResponse

def print1(request):
    return render(request,'print_to_console.html')

def print_to_console(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        print(f'User input: {user_input}')
    #return HttpResponse('Form Submitted successfully')
    a1 = {'user_input': user_input}
    return render(request,'print_to_console.html',a1)




def randomcall(request):
    return render(request,'randomotpgenerator.html')

import random
import string
def randomlogic(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        print(f'User input: {user_input}')
        a2 = int(user_input)
        ran1 = ''.join(random.sample(string.digits, k=a2))
    #return HttpResponse('Form Submitted successfully')
    b = {'ran1':ran1}
    return render(request,'randomotpgenerator.html',b)


def getdate1(request):
    return render(request,'form123.html')
import datetime
from django.shortcuts import render

from .forms import *
def get_date(request):
    if request.method == 'POST':
        form = IntegerDateForm(request.POST)
        if form.is_valid():
            integer_value = form.cleaned_data['integer_value']
            date_value = form.cleaned_data['date_value']
            updated_date = date_value + datetime.timedelta(days=integer_value)
            return render(request,'form123.html',{'updated_date':updated_date})
        else:
            form = IntegerDateForm()
        return render(request,'form123.html',{'form':form})

def get_registered(request):
    return render(request, 'anyfile.html')

from.models import *
from django.shortcuts import render, redirect
def registerloginfunction(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phonenumber = request.POST.get('phonenumber')
        if Sindhu.objects.filter(email=email).exists():
            return HttpResponse("Email already registered.Choose a different email.")
        Sindhu.objects.create(name=name, email=email, password=password, phonenumber=phonenumber)
        return redirect('newhomepage')
    return render(request,'anyfile.html')

def contact123(request):
    return render(request, 'contact.html')

from.models import *
from django.shortcuts import render, redirect
from django.core.mail import send_mail
def contactmail(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        Lastname = request.POST.get('Lastname')
        email = request.POST.get('email')
        comments = request.POST.get('comments')
        tosend = comments + '--------------this is just the copy-------------- '
        data = contactus(firstname=firstname,Lastname=Lastname, email=email, comments = comments)
        data.save()
        #return HttpResponse("<h1><center>Thank you giving Feedback
        send_mail(
            'Thank You for Contacting Sindhus Travel Tourism and management',
            tosend,
            '2200032319cseh@gmail.com',
            [email],
            fail_silently=False,
        )
        return HttpResponse("<h1><center>Mail sent</center></h1>")
    else:
        HttpResponse("<h1>error</h1>")
        # return redirect('newhomepage')
    # return render(request,'contact.html')

import matplotlib.pyplot as plt
import numpy as np

def pie_chart(request):
    if request.method == 'POST':
        form = PieChartForm(request.POST)
        if form.is_valid():
            # Process user input
            y_values = [int(val) for val in form.cleaned_data['y_values'].split(',')]
            labels = [label.strip() for label in form.cleaned_data['labels'].split(',')]

            # Create pie chart
            plt.pie(y_values, labels=labels, startangle=90)
            plt.savefig('static/images/pie_chart.png')  # Save the chart image
            img1={'chart_image': '/static/images/pie_chart.png'}
            return render(request, 'chart_form.html', img1)
    else:
        form = PieChartForm()
    return render(request, 'chart_form.html', {'form': form})

import requests

def weatherpagecall(request):
    return render(request, 'weatherappinput.html')
def weatherlogic(request):
    if request.method == 'POST':
        place = request.POST['place']
        API_KEY = '4e30ba3dcd838f557e9bdcdc536d48ad'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperature1 = round(temperature - 273.15,2)
            return render(request, 'weatherappinput.html',
                          {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
        else:
            error_message = 'City not found. Please try again.'
            return render(request, 'weatherappinput.html', {'error_message': error_message})

from django.shortcuts import render
from django.contrib.auth.models import User,auth
from django.contrib import messages

def login(request) :
    return render(request, 'login.html')
def signup(request):
    return render(request,'signup.html')
def login1(request):
    if request.method == 'POST':
        username=request.POST['username']
        pass1=request.POST['password']
        user=auth.authenticate(username=username,password=pass1)
        if user is not None :
            auth.login(request,user)
            return render(request,'newhomepage.html')
        else:
            messages.info(request,'Invalid credentials')
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def signup1(request):
 if request.method=="POST":
    username=request.POST['username']
    pass1=request.POST['password']
    pass2=request.POST['password1']
    if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'OOPS! Username already taken')
                return render(request,'signup.html')
            else:
                user=User.objects.create_user(username=username,password=pass1)
                user.save()
                messages.info(request,'Account created successfully!!')
                return render(request,'login.html')
    else:
            messages.info(request,'Password do not match')
            return render(request,'signup.html')

def logout(request):
    auth.logout(request)
    return render (request,'newhomepage.html')


