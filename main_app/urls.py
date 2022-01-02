from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('tamas/', views.tamas_index, name='tamas_index'),
  path('tamas/<int:tama_id>/', views.tamas_detail, name='tamas_detail'),
  path('tamas/create/', views.TamaCreate.as_view(), name='tamas_create'),
  path('tamas/<int:pk>/update/', views.TamaUpdate.as_view(), name='tamas_update'),
  path('tamas/<int:pk>/delete/', views.TamaDelete.as_view(), name='tamas_delete'),
  path('tamas/<int:tama_id>/add_feeding/', views.add_feeding, name='add_feeding'),
  path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
  path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
  path('toys/', views.ToyList.as_view(), name='toys_index'),
  path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
  path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
  path('tamas/<int:tama_id>/add_feeding/', views.add_feeding, name='add_feeding'),
  path('tamas/<int:tama_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
  path('accounts/signup/', views.signup, name='signup')
]