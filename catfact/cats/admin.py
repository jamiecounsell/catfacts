from django.contrib import admin
from facts.models import Fact 
admin.autodiscover()

admin.site.register(Fact)