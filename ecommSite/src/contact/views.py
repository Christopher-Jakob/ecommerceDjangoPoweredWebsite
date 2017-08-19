# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.



from .forms import contactForm

# send_mail settings in the django settings
def contact(request):
	title = 'contact'
	form =contactForm(request.POST or None)
	confirm_message = None

	if form.is_valid():
		name= form.cleaned_data['name']
		comment = form.cleaned_data['comment']
		subject = 'Its totally working yo!'
		message =  '%s %s' %(comment, name)
		emailFrom = form.cleaned_data['email']
		emailTo = [settings.EMAIL_HOST_USER]
		send_mail(
			subject,
			message,
			emailFrom,
			emailTo,
			fail_silently=True
		)
		title ="uggghh!"
		confirm_message ="Thanks for the message but we busy yo!"
		form = None

	context = {'title': title, 'form': form, 'confirm_message': confirm_message}
	template = 'contact.html'
	return render(request, template, context)
