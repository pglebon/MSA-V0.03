from django.urls import path
from django.conf.urls import include


from . import views

app_name = 'partenaire'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('Edit/<str:pk>/', views.EditPartenaire, name='EditPartenaire'),
]
