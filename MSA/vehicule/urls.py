from django.urls import path
from django.conf.urls import include

from . import views

app_name = 'vehicule'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<str:pk>/', views.detail, name='detail'),
    path('Add/', views.NewVehicule, name='NewVehicule'),
    path('Edit/<str:pk>/', views.EditVehicule, name='EditVehicule'),
    path('categories/', views.listeCategories, name='listeCategories'),
    path('editCategorie/<str:pk>/', views.editCategorie, name='editCategorie'),
    path('newCategorie/', views.newCategorie, name='newCategorie'),
    
]