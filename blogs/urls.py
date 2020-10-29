from django.urls import path
from .views import *

urlpatterns = [
    path('', blogs_home, name='blogs' ),
    path('<str:slug>/', blog_single, name='blog single')
]
