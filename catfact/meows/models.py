from django.db import models
from facts.models import Fact
from cats.models import Cat
from django.conf import settings
from twilio.rest import TwilioRestClient as TRC

class Meow(models.Model):
	cat_to   = models.ForeignKey(Cat)
	fact     = models.ForeignKey(Fact)
	date     = models.DateTimeField(auto_now_add = True)

	def send(self):

		client = TRC(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
		body = self.fact.body
		message = client.messages.create(from_=settings.TWILIO_FROM, to="+1"+str(self.cat_to.phone), body=body)
		print message

	def __unicode__(self):
		return self.fact.name + " -> " + self.cat_to.__unicode__()