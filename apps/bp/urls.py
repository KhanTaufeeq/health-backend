from django.urls import path
from . import views 


urlpatterns = [
  path('', views.list_bp, name = 'list bp'),
  path('add/', views.add_bp, name = 'add bp'),
  path('csrf/', views.csrf, name = 'csrf'),
  path('update/<int:bp_id>/', views.update_bp, name = 'update bp'),
  path('delete/<int:bp_id>/', views.delete_bp, name = 'delete bp')
]
