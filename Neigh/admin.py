from django.contrib import admin
from .models import Neighbourhood,Profile,Business, Contact

admin.site.register(Neighbourhood)
admin.site.register(Profile)
admin.site.register(Business)
admin.site.register(Contact)