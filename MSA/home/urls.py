from django.urls import path
from django.conf.urls import include

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
]
