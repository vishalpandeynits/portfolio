from django import forms
from .models import Message
from django.forms import ModelForm

class MessageForm(forms.ModelForm):
	class Meta():
		model = Message
		fields = '__all__'