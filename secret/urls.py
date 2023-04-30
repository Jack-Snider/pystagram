from django.urls import path, include
from secret.views import sender, receiver

urlpatterns = [
    path( '', sender ),
    path( 'receiver/', receiver )
]