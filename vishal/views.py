from django.shortcuts import render
from django.http import HttpResponse
from .forms import MessageForm

import re 

def isValid(s): 
	Pattern = re.compile("(0/91)?[7-9][0-9]{9}") 
	return Pattern.match(s) 

def home(request):
	message = None
	if request.method=="POST":
		form=MessageForm(request.POST)
		if form.is_valid():
			form.phone_number=request.POST.get('phone_number')
			if isValid(form.phone_number):
				message= "Your Message is sent to Vishal Pandey, He will reach you soon."
				form.save()
			elif not isValid(form.phone_number):
				message="Please Enter a valid Indian Phone Number"
	if request.method=="GET":
		form=MessageForm()
		message=None
	params= {'form':form, 'message':message}
	print(params["message"])
	return render(request,'page.html',params)