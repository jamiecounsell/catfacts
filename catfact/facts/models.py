from django.db import models

# Facts (the reason we're all here)
class Fact(models.Model):

	# Meow, name and body of fact
	name = models.CharField(max_length=100, blank=True, null=False, verbose_name="Name")
	body = models.TextField(max_length=1600, blank=True, null=False, verbose_name="Body")
	
	# CATegories. Get it?
	isSample 	= models.BooleanField(default=False,blank=True, verbose_name="Sample")
	isSatire 	= models.BooleanField(default=False,blank=True, verbose_name="Satire")
	isApathetic = models.BooleanField(default=False,blank=True, verbose_name="Apathetic")
	isConcerned = models.BooleanField(default=False,blank=True, verbose_name="Concerned")
	isNotCat 	= models.BooleanField(default=False,blank=True, verbose_name="Not Cat")
	isMythical 	= models.BooleanField(default=False,blank=True, verbose_name="Mythical")

	# can haz source?
	source 		= models.CharField(blank=True, null=True, max_length=200, verbose_name="Source")

	def __unicode__(self):
		return self.name


