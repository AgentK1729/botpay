from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from chat import *

def home(request):
	if request.method == "GET":
		return render(request, "home.html", {'STATIC_URL':settings.STATIC_URL})
	elif request.method == "POST":
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		if user:
			request.session['user'] = request.POST['username']
			login(request, user)
			return HttpResponseRedirect("/profile/")
		else:
			return render(request, "home.html", {'error':'Either the username or the password is incorrect', 'STATIC_URL':settings.STATIC_URL})
		
@login_required(login_url='/home/')
def profile(request):
	return render(request, "profile.html")

def Logout(request):
	try:
		logout(request)
	except:
		pass
	return HttpResponseRedirect("/home/")