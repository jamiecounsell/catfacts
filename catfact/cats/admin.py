from django.contrib import admin
from cats.models import Cat 
admin.autodiscover()

admin.site.register(Cat)