from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
  photo = models.ImageField(upload_to = 'photos/')
  bio = models.CharField(max_length=200)
  contact = models.EmailField()
  user = models.OneToOneField(User, on_delete=models.CASCADE)

  @receiver(post_save, sender=User)
  def create_user_profile(sender, instance, created, **kwargs):
    if created:
      Profile.objects.create(user=instance)

  @receiver(post_save, sender=User)
  def save_user_profile(sender, instance, **kwargs):
      instance.profile.save()

  post_save.connect(save_user_profile, sender=User)

  def save_profile(self):
    self.save()

  def delete_profile(self):
    self.delete()



class Business(models.Model):
  title = models.CharField(max_length=60)
  image = models.ImageField(upload_to = 'photos/')
  description = models.TextField()
  owner = models.CharField(max_length=60)
  neighbourhood = models.ForeignKey(User,on_delete=models.CASCADE)
  email = models.EmailField(max_length=60)
  pub_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title
  class Meta:
    ordering = ['title']

  def save_project(self):
    self.save()

  def delete_project(self):
    self.delete()

class Neighbor(models.Model):
  title = models.CharField(max_length=60)
  image = models.ImageField(upload_to = 'photos/')
  description = models.TextField()
  owner = models.CharField(max_length=60)
  neighbourhood = models.ForeignKey(User,on_delete=models.CASCADE)
  email = models.EmailField(max_length=60)
  pub_date = models.DateTimeField(auto_now_add=True)





  def save_rating(self):
    self.save()

  def delete_rating(self):
    self.delete()

class NeighLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()    