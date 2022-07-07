
from unicodedata import name
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from basicbank import views

urlpatterns = [
    path('', views.home, name ="home"),
    path('about/', views.about, name="about"),
    path('cust/', views.cust, name="cust"),
    path('trans/', views.trans, name="trans"),
    path('transc/', views.transc, name="transc")
]
