from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.book_club, name='book_club'),
    path('addInSubject/', views.addInSubject,name='addInSubject'),
    path('addInComments/', views.addInComments,name='addInComments'),
]
