from rest_framework.serializers import ModelSerializer, CharField, ValidationError
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
# from .utils import send_activation_code
# from .utils_2 import send_recovery_code
# from .utils_emp import send_employer_activation_code
from .tasks import send_activation_code_celery, send_recovery_code_celery, send_employer_activation_code_celery


User = get_user_model()  # возвращает активную модельку юзера


class RegisterSerializer(ModelSerializer):
    password_confirm = CharField(min_length=5, required=True, write_only=True)

    class Meta:
        model = User
        # fields = '__all__'
        fields = 'email', 'first_name', 'last_name', 'password', 'password_confirm'

    def validate(self, attrs):
        pass1 = attrs.get('password')
        pass2 = attrs.pop('password_confirm')
        if pass1 != pass2:
            raise ValidationError('Passwords do not match!')
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        send_activation_code_celery.delay(user.email, user.activation_code)
        return user


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate_email(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Пользователь не найден')
        return email

    def send_recovery_email(self):
        email = self.validated_data.get('email')
        user = User.objects.get(email=email)
        user.create_activation_code()
        send_recovery_code_celery.delay(email, user.activation_code)
        user.save()


class ForgotPasswordCompleteSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    activation_code = serializers.CharField(required=True)
    new_password = serializers.CharField(min_length=5, required=True)
    new_password_confirm = serializers.CharField(min_length=5, required=True)

    def validate(self, attrs):
        email = attrs.get('email')
        activation_code = attrs.get('activation_code')
        pass1 = attrs.get('new_password')
        pass2 = attrs.get('new_password_confirm')
        if not User.objects.filter(email=email, activation_code=activation_code).exists():
            raise serializers.ValidationError('Пользователь не найден')
        if pass1 != pass2:
            raise serializers.ValidationError('Пароли должны совпадать!')
        return attrs

    def set_new_password(self):
        email = self.validated_data.get('email')
        password = self.validated_data.get('new_password')
        user = User.objects.get(email=email)
        user.set_password(password)
        user.activation_code = ''
        user.save()


class BecomeEmployerSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=20, required=True, write_only=True)

    class Meta:
        model = User
        # fields = '__all__'
        fields = 'email', 'password'

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = User.objects.filter(email=email).first()

        if not user:
            raise serializers.ValidationError('Пользователь не найден')
        if not user.is_active:
            raise serializers.ValidationError("Пользователь не активирован.")
        if not authenticate(email=email, password=password):
            raise serializers.ValidationError('Неверный пароль!')

        attrs['user'] = user
        return attrs

    def save(self, **kwargs):
        user = self.validated_data['user']
        user.is_employer = True
        user.create_employer_activation_code()
        send_employer_activation_code_celery.delay(user.email, user.employer_activation_code)
        user.save()
        return user


