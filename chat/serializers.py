from rest_framework import serializers
from .models import Chat, Message
from account.serializers import UserSerializer

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ['chat', 'sender', 'content', 'timestamp']

class ChatSerializer(serializers.ModelSerializer):
    participant1 = UserSerializer(read_only=True)
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Chat
        fields = ['id', 'participant1', 'participant2', 'messages']
