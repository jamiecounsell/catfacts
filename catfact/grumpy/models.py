from django.db import models

class Mood(models.Model):
	name = models.CharField(max_length=100, unique=True, blank=True, null=False, verbose_name="Name")
	description = models.TextField(max_length=1600, blank=True, null=False, verbose_name="Body")

	isActive = models.BooleanField(default=False, blank=True, null=False, verbose_name="Active")
	# frequency?
	# rolls?

	# Override save to ensure only one mood is active
	def save(self, *args, **kwargs):
		if self.isActive:
			try:
				# If other mood is active, set inactive
				temp = Mood.objects.get(isActive=True)
				if self != temp:
					temp.isActive = False
					temp.save()

			# Catch Mood DNE
			except Mood.DoesNotExist:
				pass

		super(Mood, self).save(*args, **kwargs)

	# Display name
	def __unicode__(self):
		return self.name