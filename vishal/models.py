from django.db import models

# Create your models here.
class Message(models.Model):
	your_name =models.CharField("",max_length=50)
	your_email = models.EmailField("")
	phone_number = models.DecimalField("",max_digits=10,decimal_places=0)
	message = models.TextField("")
	def __str__(self):
		return self.your_email