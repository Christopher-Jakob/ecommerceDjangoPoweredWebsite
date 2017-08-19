# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import stripe

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
def checkout(request):
	publishKey = settings.STRIPE_PUBLISHABLE_KEY

	if request.method == 'POST':
		#store the token generated by stripe to be passed for a charge
		token = request.POST['stripeToken']
		try:
			charge = stripe.Charge.create(
				amount=1000, # values in cents  all these values are placeholder right now
				currency ='usd',
				source = token,
				description = "Example charge")

		except stripe.error.CardError as e:
			# declined card
			pass   
	context = {'publishKey' : publishKey}
	template = 'checkout.html'
	return render(request, template, context)

