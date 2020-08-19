from django.urls import path
from . import views

urlpatterns = [
   
   path('', views.home, name='HTA-home')
]