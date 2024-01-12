from rest_framework import serializers
from .models import Job
from django.db.models import Avg

class JobSerializers(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='user.username')
    rating = serializers.SerializerMethodField(method_name='get_rating_avg')

    def get_rating_avg(self, instance):
        rating_avg = instance.ratings.aggregate(Avg('value'))
        return rating_avg
    class Meta:
        model = Job
        fields = '__all__'
        # fields = ['id' ,'title', 'description', 'owner', 'location', 'salary', 'posted_date']


