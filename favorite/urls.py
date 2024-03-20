from django.urls import path, include
from .views import FavoritesView, FavoritesListView, RecommendedJobsView, RatingAPIView

urlpatterns = [
    path('<slug:slug>/', FavoritesView.as_view()),
    path('', FavoritesListView.as_view()),
    path('recommended_jobs/', RecommendedJobsView.as_view(), name='recommended_jobs'),
    path('rating/<slug:slug>/', RatingAPIView.as_view())

]