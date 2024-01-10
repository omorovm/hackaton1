from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import JobSerializers
from .models import Job
from .permissions import IsOwner
from favorite.models import Favorite, Like, Rating

class StandartResultPagination(PageNumberPagination):
    page_size = 20
    page_query_param= 'page'

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializers
    pagination_class = StandartResultPagination
    search_fields = ['title', 'location']
    filterset_fields = ['description']


    def get_permissions(self):
        if self.request.method in ['PATCH', 'PUT', 'DELETE']:
            return [permissions.OR(permissions.IsAdminUser(), IsOwner())]
        return [permissions.IsAuthenticatedOrReadOnly()] 

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=['POST'])
    def toggle_rating(self, request, pk=None):
        job = self.get_object()
        rating = request.user.ratings.filter(job=job)
        if favorite:
            favorite.delete()
            return Response('вы удaлили отзыв которого оставили не давно', 204)
        favorite = Favorite.objects.create(
            job=job,
            owner=request.user,
            value = request.value
        )
        return Response('вы оставили отзыв на данную вакансию', 201)

    @action(detail=True, methods=['POST'])
    def toggle_like(self, request, pk=None):
        job = self.get_object()
        like = request.user.likes.filter(job=job)
        if like:
            like.delete()
            return Response('вы удалили лайк', 204)
        like = Like.objects.create(
            job=job,
            owner=request.user
        )
        return Response('вы добавили лайк', 201)

    @action(detail=True, methods=['POST'])
    def toggle_favorite(self, request, pk=None):
        job = self.get_object()
        favorite = request.user.favorites.filter(job=job)
        if favorite:
            favorite.delete()
            return Response('удалено из избранных', 204)
        favorite = Favorite.objects.create(
            job=job,
            owner=request.user
        )
        return Response('добавлено в избранное', 201)



