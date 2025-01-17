from django.urls import path
from . import views

urlpatterns = [
  path('', views.list_data, name = "list data"),
  path('add/', views.add_sugar, name = 'add data'),
  path('csrf/', views.csrf, name = 'csrf'),
  path('delete/<int:sugar_id>/', views.delete_sugar, name = 'delete data'),
  path('update/<int:sugar_id>/', views.update_sugar, name = 'update data'),
]
