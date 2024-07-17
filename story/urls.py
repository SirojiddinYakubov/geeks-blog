from django.urls import path, include
from rest_framework import routers

from story import views

router = routers.DefaultRouter()
# router.register(r'users',views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/', views.UserViewSet.as_view(), name='user_list'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user_list'),
    path('stories/', views.StoryViewSet.as_view(), name='story_list'),
    path('stories/<int:pk>/', views.StoryDetailView.as_view(), name='story_detail'),
    path('follow-to-topics/', views.FollowToTopicView.as_view(), name='follow_to_topic_list'),
    path('follow-to-topics/<int:pk>/', views.FollowToTopicDetailView.as_view(), name='follow_to_topic_detail'),
    path('read-stories/', views.ReadStoryView.as_view(), name='read_story_list'),
    path('read-stories/<int:pk>/', views.ReadStoryDetailView.as_view(), name='read_story_detail'),
    path('claps/', views.ClapView.as_view(), name='clap_list'),
    path('claps/<int:pk>/', views.ClapDetailView.as_view(), name='clap_detail'),
    path('comments/', views.CommentView.as_view(), name='comment_list'),
    path('comments/<int:pk>/', views.CommentDetailView.as_view(), name='comment_detail'),
    path('follow-authors/', views.FollowAuthorView.as_view(), name='follow_author_list'),
    path('follow-authors/<int:pk>/', views.FollowAuthorDetailView.as_view(), name='follow_author_detail'),
    path('topics/', views.TopicView.as_view(), name='topic_list'),
    path('topics/<int:pk>/', views.TopicDetailView.as_view(), name='topic_detail'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
