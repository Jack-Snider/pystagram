from django.urls import path, include
from secret.views import secret_index, secret_intro

urlpatterns = [
    path( '', secret_index ),
    path( 'intro/', secret_intro ),
]