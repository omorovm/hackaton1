from rest_framework import serializers
from .models import Job

class JobSerializers(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Job
        fields = ['title', 'description', 'owner', 'location', 'salary', 'posted_date']

