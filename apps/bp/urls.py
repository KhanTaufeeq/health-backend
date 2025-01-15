from django.urls import path
from . import views 


urlpatterns = [
  path('', views.list_bp, name = 'list bp'),
  path('add/', views.add_bp, name = 'add bp'),
  path('csrf/', views.csrf, name = 'csrf')
]
