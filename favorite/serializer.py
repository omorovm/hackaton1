from rest_framework import serializers
from .models import Favorite
from job.models import Job


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