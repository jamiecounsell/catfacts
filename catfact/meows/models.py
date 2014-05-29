from django.db import models
from facts.models import Fact
from cats.models import Cat
from django.conf import settings
from twilio.rest import TwilioRestClient as TRC

class Meow(models.Model):
	from_cat = models.ForeignKey(Cat)
	to_cat   = models.ForeignKey(Cat)
	fact     = models.ForeignKey(Fact)
	date     = models.DateTimeField(auto_now_add = True)

	def send(self):

		client = TRC(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

		body = self.fact
		#message = client.messages.create(to=self.to_cat.)
