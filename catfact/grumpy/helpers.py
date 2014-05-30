from grumpy.models import Mood
import random
from django.conf import settings
# Return current active mood
def current_mood():
	a = Mood.objects.filter(isActive=True)
	return a[0]

# Change mood 
def change_mood():

	# Change mood based on global probability of change
	should_change = random.random() < settings.MOOD_CHANGE_PROBABILITY

	# Change the mood
	if should_change:

		moods = Mood.objects.all()

		# Choose new mood
		newMood = random.choice(moods)
		newMood.isActive = True
		newMood.save()
		
		# Return new mood
		return newMood

	# Return current mood
	else:
		print "Not changing!"
		return current_mood()