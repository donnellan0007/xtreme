from django.contrib import admin
from django.urls import path, include
from .views import index, purchase
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name="index"),
    path('purchase/', views.purchase, name="buy"),
]
