from rest_framework.serializers import ModelSerializer, ValidationError, ReadOnlyField, Serializer, SlugField, CharField
from .models import Job
from django.contrib.auth import get_user_model
from slugify import slugify
from resume.models import Resume
from django.db.models import Avg
from favorite.models import Rating
User = get_user_model()


class JobSerializer(ModelSerializer):
    who_created = ReadOnlyField(source='user')
    title = CharField(max_length=50)

    class Meta:
        model = Job
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['who_created'] = user
        return super(JobSerializer, self).create(validated_data)
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        # Получение рейтингов для каждой вакансии
        ratings = instance.ratings.all()
        average_rating = ratings.aggregate(Avg('value'))['value__avg']

        # Добавление рейтингов к представлению
        representation['ratings'] = {
            'средний рейтинг': average_rating,
            'общие рейтинги': len(ratings),
            'индивидуальные_рейтинги': [rating.value for rating in ratings]
        }

        return representation



class ApplyToJobSerializer(Serializer):
    slug = SlugField()

    def validate_slug(self, value):
        try:
            vacancy = Job.objects.get(slug=value)
        except Job.DoesNotExist:
            raise ValidationError('Такой вакансии не существует')
        return vacancy


class EmployerResumeSerializer(ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'


class UpdateResumeStatusSerializer(Serializer):
    status = CharField()

    def validate_status(self, value):
        allowed_statuses = ['viewed', 'rejected', 'contact_soon']

        if value not in allowed_statuses:
            raise ValidationError(
                f'Недопустимое значение статуса. Допустимые значения: {", ".join(allowed_statuses)}')

        return value