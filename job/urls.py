from django.urls import path
from .views import JobViewSet, EmployerGetResumeView, ApplyToJobView, UpdateResumeStatusView
from rest_framework.routers import DefaultRouter
from django.urls import include


# router = DefaultRouter()
# router.register('vacancy', VacancyViewSet)
# router.register('apply_to_vacancy', ApplyToVacancyView, basename='apply_to_vacancy')

urlpatterns = [
    path('job/', JobViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('job/<slug:slug>/', JobViewSet.as_view({'get': 'retrieve', 'patch': 'update', 'delete': 'destroy'})),
    path('apply_to/', ApplyToJobView.as_view(), name='apply_to_vacancy'),
    path('employer_retrieve_resume/<slug:slug>/', EmployerGetResumeView.as_view()),
    path('update_status/<int:resume_id>/', UpdateResumeStatusView.as_view()),

    ]