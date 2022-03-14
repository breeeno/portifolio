from django.urls import path
from webdev.principal import views

app_name = 'principal'
urlpatterns = [
    path('', views.home, name='home'),
]
