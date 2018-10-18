from django.contrib import admin
from .models import Neighbourhood,UserProfile,Business

# Register your models here.
admin.site.register(Neighbourhood)
admin.site.register(UserProfile)
admin.site.register(Business)
