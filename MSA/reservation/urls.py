from django.urls import path
from django.conf.urls import include


from . import views

app_name = 'reservation'
urlpatterns = [
    path('', views.index, name='index'),
    path('categorie/', views.choixCategorie, name='choixCategorie'),
    path('choixClient/<str:immatriculation>', views.choixClient, name='choixClient'),
    path('choixVehicule/<str:categorie>', views.choixVehicule, name='choixVehicule'),
    path('liste/', views.ListeReservation, name='ListeReservation'),
    path('add_custumer/<str:custumer>', views.add_custumer, name='add_custumer'),
    path('add_driver/<str:driver>', views.add_driver, name='add_driver'),
    path('save/', views.saveResa, name='save'),
    path('editResa/<str:pk>', views.editResa, name='editResa'),
    path('editContrat/<str:pk>', views.editContrat, name='editContrat'),
]
