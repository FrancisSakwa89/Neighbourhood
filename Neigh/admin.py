from django.contrib import admin
from .models import Neighbourhood, Business, Contact

admin.site.register(Neighbourhood)
# admin.site.register(Profile)
admin.site.register(Business)
admin.site.register(Contact)