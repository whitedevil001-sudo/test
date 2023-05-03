from django.contrib import admin
from django.urls import path,include
from .views import test_list
urlpatterns = [
    path('test/' , test_list , name='myapp'),
    
]