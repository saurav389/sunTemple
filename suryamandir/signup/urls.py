from django.urls import path
from django.contrib.auth import views
from .views import register

urlpatterns = [
    path('',register,name ='signup'),
]

