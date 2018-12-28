from rest_framework import serializers
from .models import Profile, 


class NeighbourhoodSerializer(serializers.ModelSerializer):
  class Meta:
    model = Project
    fields = ('title','image','description','owner','email','neighbourhood','pub_date')


class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields = ('photo','bio','contact','user')