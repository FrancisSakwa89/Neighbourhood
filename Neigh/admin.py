from django.contrib import admin
from .models import Neighbourhood, Business, Contact,Post,Comment

admin.site.register(Neighbourhood)
admin.site.register(Post)
admin.site.register(Business)
admin.site.register(Contact)
admin.site.register(Comment)