from .models import Resume
from .serializers import ResumeSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework import permissions

from .permissions import IsOwnerOrReadOnly, IsStuff
from .models import Resume
from .serializers import ResumeSerializer

class StandartResultPagination(PageNumberPagination):
    page_size = 20
    page_query_param= 'page'

class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    pagination_class = StandartResultPagination
    search_fields = ['title', 'location']
    filterset_fields = ['description']
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticated, IsStuff]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



