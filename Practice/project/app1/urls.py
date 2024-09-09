from django.urls import path
from app1 import views

urlpatterns=[
    # path('', views.home, name='home'),
    path('', views.firstRender, name='firstRender'),
    path('', views.myredirect, name='myredirect'),
    path('', views.myJsonResponse, name='myJsonResponse'),
]