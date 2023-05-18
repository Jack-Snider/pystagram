from django.urls import path
from users.views import login_view, logout_view, signup
from posts.views import feeds

urlpatterns = [
    path( "login/", login_view ),
    path( "logout/", logout_view ),
    path( "signup/", signup ),
]