import os
import datetime
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

# Create your models here.

def hotel_feature_image_name(instance, filename):
	#Get file expension
	ext = filename.split('.')[-1]
	#Getting current time
	current_time = datetime.datetime.now()

	filename = '{}.{}'.format(current_time, ext)
	return os.path.join('hotel_featued_image', filename)

class Destination(models.Model):
	destination_name = models.CharField(_('Destination'), max_length=255, unique=True, null=False, blank=False)
	decription = models.TextField(_('Decription'), blank=True, default='')

	created_on = models.DateTimeField(_('Created On'), auto_now_add=True)	
	updated_on = models.DateTimeField(_('Updated On'), auto_now=True)

	class Meta:
		verbose_name = "Destination"
		verbose_name_plural = "Destinations"

	def __str__(self):
		return self.destination_name

class Hotel(models.Model):
	hotel_name = models.CharField(_('Hotel'), max_length=255, blank=False, null=False, unique=True)
	destination = models.OneToOneField(Destination, on_delete=models.CASCADE)
	description = models.TextField(_('Description'), blank=True, default='')
	image = models.ImageField(_('Featured Image - 100px x 100 px'), upload_to=hotel_feature_image_name, blank=False, null=True)
	created_on = models.DateTimeField(_('Created On'), auto_now_add=True)	
	updated_on = models.DateTimeField(_('Updated On'), auto_now=True)

	class Meta:
		verbose_name = "Hotel"
		verbose_name_plural = "Hotels"

	def __str__(self):
		return self.hotel_name
	'''
	def __unicode__(self):
		return self.hotel_name
	'''
