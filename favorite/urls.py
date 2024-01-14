from django.urls import path, include
from .views import FavoritesView, FavoritesListView, RecommendedJobsView

urlpatterns = [
    path('favorites/<slug:slug>/', FavoritesView.as_view()),
    path('favorites/', FavoritesListView.as_view()),
    path('recommended_jobs/', RecommendedJobsView.as_view(), name='recommended_jobs'),

]