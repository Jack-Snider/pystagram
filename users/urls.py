from django.urls import path
from users.views import login_view
from posts.views import feeds

urlpatterns = [
    path( "login/", login_view ),
]