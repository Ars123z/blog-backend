from unicodedata import name
from django.urls import path
from .views import (
        RegisterView, 
        VerifyUserEmail,
        LoginUserView, 
        TestingAuthenticatedReq, 
        PasswordResetConfirm, 
        PasswordResetRequestView,
        SetNewPasswordView,
        ChangePasswordView, 
        LogoutApiView
        )
from rest_framework_simplejwt.views import (TokenRefreshView,)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('verify-email/', VerifyUserEmail.as_view(), name='verify'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', LoginUserView.as_view(), name='login_user'),
    path('get-something/', TestingAuthenticatedReq.as_view(), name='just_for_testing'),
    path('password-reset/', PasswordResetRequestView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name='reset_password_confirm'),
    path('set-new-password/', SetNewPasswordView.as_view(), name='set_new_password'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('logout/', LogoutApiView.as_view(), name='logout')
    ]