from django.urls import path
from .views import JobViewSet, EmployerGetResumeView, ApplyToJobView, UpdateResumeStatusView
from rest_framework.routers import DefaultRouter
from django.urls import include


# router = DefaultRouter()
# router.register('vacancy', VacancyViewSet)
# router.register('apply_to_vacancy', ApplyToJobView, basename='apply_to_vacancy')

urlpatterns = [
    path('', JobViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('<slug:slug>/', JobViewSet.as_view({'get': 'retrieve', 'patch': 'update', 'delete': 'destroy'})),
    path('apply_to/<slug:slug>/', ApplyToJobView.as_view(), name='apply_to_job'),
    path('employer_retrieve_resume/<slug:slug>/', EmployerGetResumeView.as_view()),
    path('update_status/<int:resume_id>/', UpdateResumeStatusView.as_view()),

    ]