from django.contrib import admin

from grumpy.models import Mood 
admin.autodiscover()

admin.site.register(Mood)