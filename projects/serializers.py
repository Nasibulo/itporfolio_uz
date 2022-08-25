from rest_framework import serializers
from .models import *
from users.serializers import ProfileSerializer

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    sender = ProfileSerializer(many=False, read_only=True)
    class Meta:
        model = Message
        fields = '__all__'

