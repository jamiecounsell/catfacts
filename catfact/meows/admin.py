from django.contrib import admin
from meows.models import Meow 
admin.autodiscover()

admin.site.register(Meow)