from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Neighbourhood(models.Model):
  name = models.CharField(max_length=60,default='name')
  image = models.ImageField(upload_to = 'photos/')
  location = models.CharField(max_length=60)
  occupants_count = models.PositiveIntegerField()
  email = models.EmailField(max_length=60,default='email')
  # pub_date = models.DateTimeField(auto_now_add=True,default='dat')


  def save_neighbourhood(self):
    self.save()

  def delete_neighbourhood(self):
    self.delete()




class Profile(models.Model):
  photo = models.ImageField(upload_to = 'photos/')
  bio = models.CharField(max_length=200)
  contact = models.EmailField()
  neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE,blank=True,null=True)
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
  name = models.CharField(max_length=60)
  email = models.EmailField()
  neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)

  def __str__(self):
    return self.name
  class Meta:
    ordering = ['name']

  def save_business(self):
    self.save()

  def delete_business(self):
    self.delete()


class NeighLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()    

class Comment(models.Model):
  comment = models.TextField()
  neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
  postername = models.CharField(max_length=60)
  pub_date = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
  name = models.CharField(max_length=60)
  post = models.TextField()
  poster = models.ForeignKey(User,on_delete=models.CASCADE)
  postername = models.CharField(max_length=60)
  neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
  pub_date = models.DateTimeField(auto_now_add=True)

class Contact(models.Model):
  name = models.CharField(max_length=140)
  contact = models.CharField(max_length=60)
  email = models.EmailField()
  neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
