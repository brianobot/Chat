from django.urls import path

from .views import UserView, LoginApiView, SignupApiView, logout_user


urlpatterns = [
    path("api/v1/users/", UserView.as_view(), name="user-list"),
    path("api/v1/login/", LoginApiView.as_view(), name="login"),
    path("api/v1/signup/", SignupApiView.as_view(), name="sign-up"),
    path("logout/", logout_user, name="logout"),
]
