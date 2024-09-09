from django.urls import path
from .import views #from app import views

urlpatterns = [
    path('', views.home, name='home')
]