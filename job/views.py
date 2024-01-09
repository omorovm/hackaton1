from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination


from .serializers import JobSerializers
from .models import Job
from .permissions import IsOwner

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




