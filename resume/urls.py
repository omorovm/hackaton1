from rest_framework.urls import path
from .views import ResumeView, ResumeDetailView

urlpatterns = [
    path('', ResumeView.as_view()),
    path('<int:pk>/', ResumeDetailView.as_view()),
]
