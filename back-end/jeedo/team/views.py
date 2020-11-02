from django.shortcuts import render
#from rest_framework.filters import SearchFilter
from .serializers import TeamMemberProfileSerializer
from .models import HomeTeam
from rest_framework.generics import ListCreateAPIView


# Create your views here.

class HomeTeamList(ListCreateAPIView):
    queryset = HomeTeam.objects.all()
    serializer_class=TeamMemberProfileSerializer