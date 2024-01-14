from rest_framework.urls import path
from .views import (RegisterView, ActivationView, ForgotPasswordView,
                    ForgotPasswordCompleteView, BecomeEmployerView,
                    BecomeEmployerCompleteView, DeleteUserView)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('activate/<str:email>/<str:activation_code>/', ActivationView.as_view(), name='activate'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('forgot_password/', ForgotPasswordView.as_view(), name='forgot_password'),
    path('forgot_password_complete/', ForgotPasswordCompleteView.as_view()),
    path('become_employer/', BecomeEmployerView.as_view()),
    path('become_employer/<str:email>/<str:employer_activation_code>/', BecomeEmployerCompleteView.as_view(),
         name='become_employer_complete'),
    path('delete/', DeleteUserView.as_view()),
]

