from django.db import models

from django.conf import settings
# Create your models here.
class About(models.Model):
	name= models.CharField(max_length=20)
	logo = models.ImageField(upload_to='ammat/', default='me.png')
	about = models.TextField()
	phone = models.TextField()
	email = models.TextField()
	facebook= models.TextField()
	Twitter = models.CharField(max_length=20)
	youtube= models.TextField()

	def publish(self):
		self.save()

	def __str__(self):
		return self.name

