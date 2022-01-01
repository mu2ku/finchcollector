from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('tamas/', views.tamas_index, name='tamas_index'),
  path('tamas/<int:tama_id>/', views.tamas_detail, name='tamas_detail'),
  path('tamas/create/', views.TamaCreate.as_view(), name='tamas_create'),
  path('tamas/<int:pk>/update/', views.TamaUpdate.as_view(), name='tamas_update'),
  path('tamas/<int:pk>/delete/', views.TamaDelete.as_view(), name='tamas_delete'),
]