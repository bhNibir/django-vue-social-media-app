from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('posts/', views.posts_page, name='posts'),
    path('groups/', views.groups, name='groups')
]
