from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from .models import *

# Create your views here.
def home(request):
    tank_readings = TankReading.objects.all()
    moisture_readings = MoistureReading.objects.all()
    temperature_readings = TemperatureReading.objects.all()
    lighting_readings = LightingReading.objects.all()
    humidity_readings = HumidityReading.objects.all()
    
    # for ordering or getting most recent TankReading.objects.all().order_by('-time')[:1]
    _context = {
	    'tank': tank_readings, 
	    'moisture': moisture_readings,
	    'temperature': temperature_readings, 
	    'lighting': lighting_readings,
	    'humidity': humidity_readings
	}
    return render(request=request, template_name='home.html', context=_context)

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, "Registration successful for " + user)
			return redirect(reverse('pages:login'))
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect(reverse('pages:home'))
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("pages:home")

class ConnectPageView(TemplateView):
    template_name = "connect.html"

def index(request):
    return HttpResponse("Hello")