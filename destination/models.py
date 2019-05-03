from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

# Create your models here.

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