from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Neighbourhood(models.Model):
    hood_name = models.CharField(max_length=50)
    hood_location = models.CharField(max_length=50)
    # hood_address = AddressField(max_length= 50, default="")
    hood_count = models.PositiveIntegerField()
    # admin = ForeignKey(Admin)

    def save_hood(self):
        self.save()
        
    def delete_hood(self):
        self.delete()
    
    @classmethod
    def search_hood(cls, search_term):
        hoods = cls.objects.filter(name__icontains = search_term)
        return hoods

    def __str__(self):
        return self.hood_name

class Business(models.Model):
    biz_name = models.CharField(max_length=50)
    biz_email = models.EmailField()
    biz_description = models.CharField(max_length=1000)
    hood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save_biz(self):
        self.save()

    def delete_biz(self):
        self.delete()


    @classmethod
    def search_biz(cls, search_term):
        business = cls.objects.filter(name__icontains=search_term)
        return business

    def __str__(self):
        return self.biz_name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_bio = models.TextField(max_length=200)

    def __str__(self):
        return self.user

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.profile.save()

class Join(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    hood_id = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user_id

class Posts(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.CharField(max_length = 1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    def __str__(self):
        return self.comment



