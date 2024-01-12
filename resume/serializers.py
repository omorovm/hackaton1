from rest_framework import serializers
from .models import Resume
from django.contrib.auth.models import User
from job.models import Job
from rest_framework.serializers import ValidationError
# from .utils_resume import send_resume_data
# User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']


class ResumeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    email = serializers.ReadOnlyField(source='user.email')
    date_of_birth = serializers.DateField(format='%d.%m.%Y', input_formats=['%d.%m.%Y'])

    class Meta:
        model = Resume
        exclude = ['profile_photo']


    def validate_sex(self, value):
        allowed_sex = ['f', 'm']

        if value not in allowed_sex:
            raise ValidationError(
                f'Недопустимое значение статуса. Допустимые значения: {", ".join(allowed_sex)}')

        return value

