from django.urls import path
from .views import AspirantProfileAPIView,ExpertProfileAPIView
from .views import AuthenticationCheckAPIView,LoginAPIView,LogoutAPIView,CSRFTokenAPIView
urlpatterns =[
    path('csrf_token/',CSRFTokenAPIView.as_view(),name='token'),
    path('login/',LoginAPIView.as_view(),name = 'login'),
    path('logout/',LogoutAPIView.as_view(),name='logout'),
    path('auth-check',AuthenticationCheckAPIView.as_view(),name='auth-check'),
    path('register_as_aspirant/',AspirantProfileAPIView.as_view(),name = 'register aspirant'),
    path('register_as_expert/',ExpertProfileAPIView.as_view(),name ='register expert' ),
]
