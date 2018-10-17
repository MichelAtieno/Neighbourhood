from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighbourhood(models.Model):
    hood_name = models.CharField(max_length=50)
    hood_location = models.CharField(max_length=50)
    hood_count = models.PositiveIntegerField(null=True)
    # admin = ForeignKey(Admin)
    def save_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()


class User(models.Model):
    user_photo = models.ImageField(upload_to='pictures/', default="")
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    hood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)

class Business(models.Model):
    biz_name = models.CharField(max_length=50)
    biz_email = models.CharField(max_length=100)
    biz_description = models.CharField(max_length=1000)
    hood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save_biz(self):
        self.save()

    def delete_biz(self):
        self.delete()


