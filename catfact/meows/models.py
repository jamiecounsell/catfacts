from django.db import models
from facts.models import Fact
from cats.models import Cat
from django.conf import settings

class Meow(models.Model):
	from_cat = models.ForeignKey(Cat)
	to_cat   = models.ForeignKey(Cat)
	fact     = models.ForeignKey(Fact)
	date     = models.DateTimeField(auto_now_add = True)

	def send(self):

