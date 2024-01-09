from rest_framework import serializers
from .models import Resume

class ResumeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Resume
        fields = ['id', 'title', 'summary', 'owner', 'skills', 'experience', 'education', 'created_at']
