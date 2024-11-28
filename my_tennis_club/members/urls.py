from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Homepage'),
    path('about', views.about, name='AboutPage'),
    path('members', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details')
]
