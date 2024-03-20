from django.db.models import Q
from rest_framework.views import APIView
from .models import Favorite
from rest_framework.response import Response
from .serializer import FavoritesSerializer, FavoriteJobSerializer
from job.models import Job
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from functools import reduce


class FavoritesView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, slug, *args, **kwargs):
        favorite_job = get_object_or_404(Job, slug=slug)
        user = request.user
        favorite_entry = Favorite.objects.filter(user=user, favorite_job=favorite_job).first()

        if favorite_entry:
            favorite_entry.delete()
            return Response('Вакансия удалена из избранного.')
        else:
            Favorite.objects.create(user=user, favorite_job=favorite_job)
            return Response('Вакансия добавлена в избранное.')


class FavoritesListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        favorites = Favorite.objects.filter(user=user)
        serializer = FavoritesSerializer(favorites, many=True)
        return Response(serializer.data)


class RecommendedJobsView(APIView):
    def get(self, request, *args, **kwargs):
        user_skills = request.user.resume.first().skills
        user_skills_list = user_skills.split(',')
        recommended_vacancies = Job.objects.filter(
            reduce(lambda x, y: x | y, [Q(requirements__contains=skill) for skill in user_skills_list])
        )

        serialized_vacancies = FavoriteJobSerializer(recommended_vacancies, many=True)
        return Response(serialized_vacancies.data)