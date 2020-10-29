from django.urls import path
from .import views

urlpatterns=[
    path('team/',views.HomeTeamList.as_view(),name ='team_list')
    
]