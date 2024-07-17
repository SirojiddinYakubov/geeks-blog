from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import viewsets, permissions, generics

from story.filters import TopicFilter
from story.models import *
from story.serializers import *
from user.models import CustomUser


class StoryViewSet(generics.ListCreateAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer

    def get_queryset(self):
        return Story.objects.all()


class StoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer


class UserViewSet(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all().order_by('-id')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class FollowToTopicView(generics.ListCreateAPIView):
    queryset = FollowToTopic.objects.all()
    serializer_class = FollowToTopicSerializer


class FollowToTopicDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FollowToTopic.objects.all()
    serializer_class = FollowToTopicSerializer


class ReadStoryView(generics.ListCreateAPIView):
    queryset = ReadStory.objects.all()
    serializer_class = ReadStorySerializer


class ReadStoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReadStory.objects.all()
    serializer_class = ReadStorySerializer


class ClapView(generics.ListCreateAPIView):
    queryset = Clap.objects.all()
    serializer_class = ClapSerializer


class ClapDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clap.objects.all()
    serializer_class = ClapSerializer


class CommentView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class FollowAuthorView(generics.ListCreateAPIView):
    queryset = FollowAuthor.objects.all()
    serializer_class = FollowAuthorSerializer


class FollowAuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FollowAuthor.objects.all()
    serializer_class = FollowAuthorSerializer


class TopicView(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TopicFilter


class TopicDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
