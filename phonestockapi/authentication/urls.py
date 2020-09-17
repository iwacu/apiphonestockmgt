from django.urls import path
from .views import RegisterView,VerifyEmail,LoginAPIView, RequestPasswordResetEmail,PasswordTokenCheckAPI,SetNewPasswordAPIView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('Login/', LoginAPIView.as_view(), name="Login"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
    path('request-reset-email/', RequestPasswordResetEmail.as_view(),
         name="request-reset-email"),
    path('password-reset/<uidb64>/<token>/',
         PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('password-reset-complete', SetNewPasswordAPIView.as_view(),
         name='password-reset-complete')     
]