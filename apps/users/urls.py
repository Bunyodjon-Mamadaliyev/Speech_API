from django.urls import path

from .views import LoginView, RefreshTokenView, RegisterView, UserProfileView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("refresh/", RefreshTokenView.as_view(), name="token_refresh"),
    path("user/profile/", UserProfileView.as_view(), name="user-profile"),
]
