# -*- coding: utf-8
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import stripe

# Create your views here.

# do not use locals for context it puts everything in context which doesn't
# work if you do not want to hide some things based on user usage
def home(request):
	context = {}
	template = 'home.html'
	return render(request,template,context)


def about(request):
	context = {}
	template = 'about.html'
	return render(request,template,context)

@login_required
def userProfile(request):
	user = request.user
	context = {'user':user}
	template = 'profile.html'
	return render(request,template,context)

