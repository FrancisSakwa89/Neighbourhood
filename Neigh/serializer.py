from rest_framework import serializers
from .models import Profile,Neighbourhood 


class NeighbourhoodSerializer(serializers.ModelSerializer):
  class Meta:
    model = Neighbourhood
    fields = ('title','image','description','owner','email','neighbourhood','pub_date')


class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields = ('photo','bio','contact','user')