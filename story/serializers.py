from rest_framework import serializers

from .models import *
from user.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'birth_date']


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'title', 'created_at']


class StorySerializer(serializers.ModelSerializer):
    topics = TopicSerializer(many=True, read_only=True)
    class Meta:
        model = Story
        fields = ['id', 'title', 'status', 'views_count','topics']


class FollowToTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowToTopic
        fields = ['id', 'user', 'topic']


class ReadStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadStory
        fields = ['id', 'story', 'user']


class ClapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clap
        fields = ['id', 'story', 'user', 'count']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'comment', 'message']


class FollowAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowAuthor
        fields = ['id', 'user', 'author']