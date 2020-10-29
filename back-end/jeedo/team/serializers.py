from rest_framework import serializers
from django.contrib.auth.models import User
from .models import HomeTeam
from accounts.models import AspirantProfile,ExpertProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User 
        fields=['username','first_name','last_name','email']

class AspirantProfileSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    #fields=['first_name','last_name','email']

    class Meta:
        model= AspirantProfile
        fields='__all__'

class ExpertProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    #fields =['first_name','last_name','email']

    class Meta:
        model= ExpertProfile
        fields='__all__'

class TeamMemberProfileSerializer(serializers.ModelSerializer):
    user= UserSerializer(read_only=True)
    #fields=['first_name','last_name','email']

    class Meta:
        model= HomeTeam
        fields="__all__"





