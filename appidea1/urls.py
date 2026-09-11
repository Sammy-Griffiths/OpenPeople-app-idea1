from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('levels/', views.levels, name='levels'),
    path('addnew/', views.add_chemical, name='add_chemical')
]