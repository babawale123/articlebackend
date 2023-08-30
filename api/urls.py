from django.urls import path,include
from .views import UserRegistration,UserLogin,ALLUser

urlpatterns = [
    path('',UserRegistration),
    path('login/',UserLogin),
    path('users/',ALLUser.as_view())
]