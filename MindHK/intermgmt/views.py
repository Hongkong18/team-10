# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
#from django.utils import simplejson

from .models import *








def index(request):
	return render(request, 'intermgmt/calendar.html')
	# event_list = Event.objects.order_by('name')
	# context = { # always a dictionary
	# 	'event_list': event_list,
	# }
	# return render(request, 'intermgmt/index.html', context)
def event(request):
	return render(request, 'intermgmt/event.html')

def resultvol(request):
	return render(request, 'intermgmt/resultVolunteers.html')

def selectvol(request):
	return render(request, 'intermgmt/selectVolunteers.html')

def balance(request):
	return render(request, 'intermgmt/event_balance.html')	

#Authentication Procedure
def login_view(request):
    if request.method == 'GET': #loading the log in page
        return render(request, 'intermgmt/login.html')
    if not request.user.is_authenticated:
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None: # a valid user
                login(request, user)
                return redirect('intermgmt:index')#portfolio
            else: # a invalid user
                return render(request, 'intermgmt/login.html', {'message': "Invalid Credentials"})
        except Exception as e:
            print(e)
            return render(request, 'intermgmt/login.html', {'message': "Invalid Credentials"})
    else:#when cached user re-visit
        return redirect('intermgmt:index')#portfolio

def signup(request):
    if request.method == 'GET':
        return render(request, 'intermgmt/signup.html')
    if not request.user.is_authenticated:
        try:
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            new_user = User.objects.create_user(username=username, email=email, password=password)
            if new_user is not None:
                return redirect('intermgmt:login')
            else:
                return render(request, 'intermgmt/signup.html', {'message': "Invalid Credentials"})
        except Exception as e:
            return render(request, 'intermgmt/signup.html', {'message': "Invalid Credentials"})
    else:
        return redirect('intermgmt:login')#portfolio

def logout_view(request):
    logout(request)
    return redirect('intermgmt:index')


