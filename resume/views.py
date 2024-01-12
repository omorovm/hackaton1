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
    pagination_class = StandartResultPagination

    def get_permissions(self):
        if self.request.method in ['PATCH', 'PUT', 'DELETE']:
            return [permissions.IsAdminUser(), IsOwner()]
        return [permissions.IsAuthenticated()]
    
    
    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            specialization = serializer.validated_data.get('specialization')
            self.validate_specialization(specialization)
            serializer.save(user=self.request.user)
        else:
            raise ValidationError('Пользователь не аутентифицирован')

    @swagger_auto_schema(request_body=ResumeSerializer())
    def post(self, request):
        serializer = ResumeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response('Ваше резюме успешно размещено на сайте! Проверьте почту')

    def get(self, request):
        users_resume = Resume.objects.filter(user=request.user)
        # Выполняем пагинацию
        page = self.paginate_queryset(users_resume)

        if page is not None:
            serializer = ResumeSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ResumeSerializer(users_resume, many=True)
        return Response(serializer.data)
    

class ResumeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_permissions(self):
        if self.request.method in ['PATCH', 'PUT', 'DELETE']:
            return [permissions.IsAdminUser(), IsOwner()]
        return [permissions.IsAuthenticated()]