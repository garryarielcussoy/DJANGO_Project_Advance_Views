from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'alphatech'
urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('mentor/', views.mentor, name='mentor'),
    path('mentee/', views.mentee, name='mentee'),
    path('author/', views.author, name='author'),
    path('forms/', views.forms, name='forms'),
    path('submit_form/', views.submit_form, name="submit_form"),
    path('<int:blog_id>/', views.read_more, name="read_more")
]