from django.contrib.auth import login,logout
from django.shortcuts import reverse,redirect
#from django.views.generic import CreateView
#from .forms import AspirantRegistrationForm,ExpertRegistraionForm
from accounts.models import AspirantProfile, ExpertProfile
from django.middleware import csrf
from django.conf import settings
from django.views.decorators.cache import never_cache
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator

import requests

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser   


class AuthenticationCheckAPIView(APIView):
    permission_classes =(AllowAny,)
    def get(self,request,*args,**kwargs):
        authenticated = request.user.is_authenticated
        data ={
            'message': "Authorized" if authenticated else 'Unauthorized'
        }
        if authenticated:
            data['user']=UserSerializer(request.user).data
            expert = ExpertProfile.objects.filter(user = request.user)
            aspirant = AspirantProfile.objects.filter(user=request.user)
            if aspirant.exists():
                data['aspirantprofile'] = AspirantProfileSerializer(aspirant.first()).data
            elif expert.exists():
                data['expertprofile'] = ExpertProfileSerializer(expert.first()).data
            else:
                data['userprofile']=False
        status_code = status.HTTP_200_OK if authenticated else status.HTTP_401_UNAUTHORIZED
        return Response(data,status=status_code)

class LoginAPIView(APIView):
    permission_classes =(AllowAny,)
    
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)

    def post(self,request):
        username = request.data.get('username',None)
        password = request.data.get('password',None)
        if username and password:
            user_obj = User.objects.filter(username=username)
            if user_obj.exists() and user_obj.first().check_password(password):
                user = UserSerializer(user_obj)
                data_List ={}
                data_List.update(user.data)
                return Response({'message':'Login Successful','data':data_List,'status':status.HTTP_200_OK200})
            else:
                message = 'Unable to login with given credentials'
                return Response({'message':message,'status':status.HTTP_500_INTERNAL_SERVER_ERROR})    
        else:
            message = 'Invalid credentials'
            return Response({'message':message,'status':status.HTTP_500_INTERNAL_SERVER_ERROR})

class LogoutAPIView(APIView):
    @method_decorator(never_cache)
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)


    def get(self,request,*args,**kwargs):
        logout(request)
        return Response({'message':'Successfully Logged out','status':status.HTTP_200_OK})    

class CSRFTokenAPIView(APIView):
    permission_classes = (AllowAny,)

    @method_decorator(never_cache)
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
    
    def get(self,request,*args,**kwargs):
        token = csrf.get_token(request)
        return Response({'csrftoken':token, 'status':status.HTTP_200_OK})

class AspirantProfileAPIView(APIView):
    permission_classes=(IsAuthenticated,IsAdminUser,)

    @method_decorator(never_cache)
    @method_decorator(csrf_protect)

    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        data={}
        for key in request.data.keys():
            data[key]=request.data.get(key)
        user = request.user
        user.first_name = data.pop('first_name')
        user.last_name = data.pop('last_name')
        user.save()
        profile = AspirantProfile.objects.create(user=user,**data)
        profile.save()
        AspirantProfile.student_register_email.delay(user.first_name,user.email)
        return Response(AspirantProfileSerializer(profile).data,status=status.HTTP_200_OK)

class ExpertProfileAPIView(APIView):
    permission_classes =(IsAdminUser,IsAuthenticated,)

    @method_decorator(never_cache)
    @method_decorator(csrf_protect)

    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        data={}
        for key in request.data.keys():
            data[key]= request.data.get(key)
        user.first_name = data.pop('first_name')
        user.last_name = data.pop('last_name')
        user.save()
        profile = ExpertProfile.objects.create(user=user,**data)
        profile.save()
        ExpertProfile.expert_register_email(user.first_name,user.email)
        return Response(ExpertProfileSerializer(profile).data,status=status.HTTP_200_OK)









