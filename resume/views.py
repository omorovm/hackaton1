from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import ValidationError
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.viewsets import generics


from .serializers import ResumeSerializer
from .permissions import  IsOwner
from .models import Resume
from .serializers import ResumeSerializer

class StandartResultPagination(PageNumberPagination):
    page_size = 2
    page_query_param= 'page'


class ResumeView(APIView):
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            raise ValidationError('Пользователь не аутентифицирован')

    @swagger_auto_schema(request_body=ResumeSerializer())
    def post(self, request):
        serializer = ResumeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response('Ваше резюме успешно размещено на сайте!')

    def get(self, request):
        users_resume = Resume.objects.filter(user=request.user)
        serializer = ResumeSerializer(users_resume, many=True)
        return Response(serializer.data)
    

class ResumeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

    def get_permissions(self):
        if self.request.method in ['PATCH', 'PUT', 'DELETE']:
            return [permissions.OR(permissions.IsAdminUser(), IsOwner())]
        return [permissions.IsAuthenticated()]
