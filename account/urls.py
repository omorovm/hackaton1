from .views import *
from django.urls import path


urlpatterns = [
    path('register/', UserRegistration.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('<int:id>/', UserDetailAPIView.as_view()),
    path('', UserListAPIView.as_view()),
    # path('resume/', include(router.urls))
]
