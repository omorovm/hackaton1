from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, generics
from .serializers import (RegisterSerializer, ForgotPasswordSerializer, ForgotPasswordCompleteSerializer,
                          BecomeEmployerSerializer)
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner
from drf_yasg.utils import swagger_auto_schema


User = get_user_model()


class RegisterView(APIView):
    @swagger_auto_schema(request_body=RegisterSerializer())             # для отображения заполняемых полей в свагере
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Вы успешно зарегистрировались! Проверьте почту и активируйте аккаунт.',
                        status=201)


class ActivationView(APIView):
    def get(self, request, email, activation_code):
        user = User.objects.filter(email=email, activation_code=activation_code).first()
        if not user:
            return Response('User does not exist', status=400)
        user.is_active = True
        user.activation_code = ''
        user.save()
        return Response('Вы успешно активировались!', status=200)


class ForgotPasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.send_recovery_email()
        return Response('Вам был отправлено сообщение для восстановления пароля')


class ForgotPasswordCompleteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ForgotPasswordCompleteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.set_new_password()
        return Response('Пароль успешно обновлен')


class BecomeEmployerView(APIView):
    @swagger_auto_schema(request_body=BecomeEmployerSerializer())        # для отображения заполняемых полей в свагере
    def post(self, request):
        serializer = BecomeEmployerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            'Вы отправили запрос на доступ к размещению вакансий. Проверьте почту и продолжите по инструкции, приложенной в сообщении',
                        status=201)


class BecomeEmployerCompleteView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, email, employer_activation_code):
        user = User.objects.filter(email=email, employer_activation_code=employer_activation_code).first()
        if not user:
            return Response('User does not exist', status=400)
        user.is_employer = True
        user.employer_activation_code = ''
        user.save()
        return Response('Вы успешно активировались в качестве работодателя!', status=200)


class DeleteUserView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        user = request.user
        user.delete()
        return Response('Пользователь успешно удален')
