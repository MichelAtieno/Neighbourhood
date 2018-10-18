from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django_google_maps.fields import AddressField, GeoLocationField

# Create your models here.
class Neighbourhood(models.Model):
    hood_name = models.CharField(max_length=50)
    hood_location = GeoLocationField(blank=True)
    hood_address = AddressField(max_length= 50, default="")
    # hood_count = models.PositiveIntegerField(null=True)
    # admin = ForeignKey(Admin)
    def __str__(self):
        return self.hood_name

class Business(models.Model):
    biz_name = models.CharField(max_length=50)
    biz_email = models.CharField(max_length=100)
    biz_description = models.CharField(max_length=1000)
    hood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.business_name

    @classmethod
    def get_business(cls, username):
        business = Business.objects.filter(user__username=username)
        return business

class UserProfile(models.Model):
    user_photo = models.ImageField(upload_to='pictures/', default="")
    user_name = models.CharField(max_length=50,  default="")
    email = models.CharField(max_length=100)
    hood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    user_profile = models.OneToOneField(settings.AUTH_USER_MODEL)

    @classmethod
    def get_user_profile(cls, username):
        profile = UserProfile.objects.get(user_profile__username = username)
        return profile

    def __str__(self):
        return self.user_profile.username

def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
    if created:
        try:
            UserProfile.objects.create(user_profile=instance)
        except Exception as error:
            print(error)

post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)



    


