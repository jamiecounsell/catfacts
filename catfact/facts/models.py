from django.db import models
from grumpy.models import Mood

# Facts (the reason we're all here)
class Fact(models.Model):

	# Meow, name and body of fact
	name = models.CharField(max_length=100, blank=True, null=False, verbose_name="Name")
	body = models.TextField(max_length=1600, blank=True, null=False, verbose_name="Body")
	# TODO: image field

	# CATegories. Get it?
	mood = models.ManyToManyField(Mood)

	# can haz source?
	source 		= models.CharField(blank=True, null=True, max_length=200, verbose_name="Source")

	def __unicode__(self):
		return self.name


