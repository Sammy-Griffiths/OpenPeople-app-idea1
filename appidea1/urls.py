from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('levels/', views.levels, name='levels'),
    path('addnew/', views.add_product, name='add_product'),
    path('controlpanel/', views.control_panel, name='control_panel'),
    path('controlpanel/clear/', views.clear_database, name='clear_database'),
]
