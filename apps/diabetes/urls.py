from django.urls import path
from . import views

urlpatterns = [
  path('', views.list_data, name = "list data"),
  path('add/', views.add_sugar, name = 'add data'),
  path('csrf/', views.csrf, name = 'csrf'),
]
