from django.urls import path, include
from secret.views import secret_index

urlpatterns = [
    path( '', secret_index ),
]