from rest_framework import serializers
from .models import Favorite, Rating
from job.models import Job
from rest_framework.serializers import ValidationError


class FavoriteJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['title', 'requirements']


class FavoritesSerializer(serializers.ModelSerializer):
    job_title = serializers.CharField(source='favorite_job.title', read_only=True)
    job_resp = serializers.CharField(source='favorite_job.responsibilities', read_only=True)

    class Meta:
        model = Favorite
        fields = ['job_title', 'job_resp']



class RatingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    value = serializers.IntegerField()

    class Meta:
        model = Rating
        fields = '__all__'

    def validate_value(self, value):
        if value not in [1, 2, 3, 4, 5]:
            raise serializers.ValidationError('Дайте значение от одного до пяти')
        return value

    def create(self, validated_data):
        user = self.context['request'].user
        job_slug = self.context['view'].kwargs['slug']
        
        try:
            job = Job.objects.get(slug=job_slug)
        except Job.DoesNotExist:
            raise serializers.ValidationError('Такой вакансии не существует')

        return Rating.objects.create(user=user, rating_job=job, **validated_data)