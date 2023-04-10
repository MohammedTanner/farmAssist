from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from datetime import datetime, timedelta

# Create your views here.
def home(request):
    tank_readings = TankReading.objects.all().order_by('-time')[:1]
    moisture_readings = MoistureReading.objects.all().order_by('-time')
    temperature_readings = TemperatureReading.objects.all().order_by('-time')
    lighting_readings = LightingReading.objects.all().order_by('-time')
    humidity_readings = HumidityReading.objects.all().order_by('-time')
    product_crops = ProductCrop.objects.all()
    slot1 = ProductCrop.objects.get(cropid=1)
    
    # for ordering or getting most recent TankReading.objects.all().order_by('-time')[:1]
    _context = {
	    'tank': tank_readings, 
	    'moisture': moisture_readings,
	    'temperature': temperature_readings, 
	    'lighting': lighting_readings,
	    'humidity': humidity_readings,
	    'crop': product_crops,
	    'slot1': slot1,
	}
    return render(request=request, template_name='home.html', context=_context)

def connect(request):
    
    meetups = Meetup.objects.select_related('creatorid').all()
    comments = MeetupComment.objects.all()
    users = AuthUser.objects.all()
    _context = {
	    'meetup': meetups,
	    'comment': comments,
	    'users': users,
	}
    return render(request=request, template_name='connect.html', context=_context)

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

def create_event(request):
	if request.user.is_authenticated:
		user = AuthUser.objects.get(username=request.user)
		en=Meetup(title=request.POST.get('title'), creatorid=user,location=request.POST.get('location'), starttime=request.POST.get('time')
	   	, date=request.POST.get('date'),description=request.POST.get('description'))
		en.save()
		return redirect("pages:connect")
	else:
		messages.error(request,"Please, login before creating an event.")
		return redirect("pages:login")

def add_comment(request):
	# add way to figure out which post to relate comment to
	if request.user.is_authenticated:
		user = AuthUser.objects.get(username=request.user)
		meetup = Meetup.objects.get(postid=request.POST.get('post'))
		en=MeetupComment(post=meetup, content=request.POST.get('comment'), username=user)
		en.save()
		return redirect("pages:connect")
	else:
		messages.error(request,"Please, login before creating an event.")
		return redirect("pages:login")

def change_crops(request):
	if request.user.is_authenticated:
		user = AuthUser.objects.get(username=request.user)
		location = 1
		updates = [request.POST.get("slot1"), request.POST.get("slot2"), request.POST.get("slot3"), request.POST.get("slot4")]
		for update in updates:
			if update == 0:
				location += 1
				continue
			else:
				new_type = Crop.objects.get(name=update)
				plant_date = datetime.now()
				product_crop = ProductCrop.objects.get(cropid=location)
				product_crop.type = new_type
				harvest_date = plant_date + timedelta(days=new_type.harvest)
				product_crop.plantdate = plant_date.strftime('%Y-%m-%d')
				product_crop.harvestdate = harvest_date.strftime('%Y-%m-%d')
				product_crop.save()
				location += 1
		return redirect("pages:home")
	else:
		messages.error(request,"Please, login before creating an event.")
		return redirect("pages:login")
	
def index(request):
    return HttpResponse("Hello")