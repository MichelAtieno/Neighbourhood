from django.contrib import admin
from .models import Neighbourhood,UserProfile,Business, Posts,Comment

# Register your models here.
admin.site.register(Neighbourhood)
admin.site.register(UserProfile)
admin.site.register(Business)
admin.site.register(Posts)
admin.site.register(Comment)
