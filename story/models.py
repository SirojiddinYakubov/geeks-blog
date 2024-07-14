from django.contrib.auth import get_user_model
from django.db import models

from core.settings import WORDS_PER_MINUTE

User = get_user_model()
"""
class Story: 
    - title: str (max_lenght: 255)
    - content: str (max_length: 5000)
    - status (draft, publish, archive, pending, reject, trash )
    - created_at: datetime
    - updated_at: datetime
    - views_count: int (min: 0)
    - read_time: int (property) 60 ta so'z 1 minut
    - topics: Topic (ManyToManyField) +

class ReadStory
    - story_id: Story
    - user_id: User
    - created_at: datetime


class Clap:
    - story_id: Story
    - user_id: User
    - count: int (min: 0, max: 50)
    
class Comment:
    - comment_id: Comment (blank=True, null=True)
    - message: str
    - user_id: User
    - created_at: datetime
    
    
class User(AbstractUser):
    + username: str
    + first_name: str
    + last_name: str
    - avatar: str (users/avatars/sirojiddinyakubov.jpg)
    - headline: str (Masalan: Jonny)
    - bio: str
    - name: str (property: last_name + first_name)
    - birth_date: date
    - age (property: 2024 - birth_date)
    + email: str
    
    
class Topic:
    - title: str
    - created_at: datetime


class FollowToTopic:
    - user_id: User
    - topic_id: Topic
    - created_at: datetime
    
    
class FollowToAuthor:
    - author_id: User
    - user_id: User
    - created_at: datetime
    
    
static vs media - done
configure custom user - done
AbstactUser vs AbstractBaseUser - done
user_id or user in ForeignKey?
user groups and permissions? - done
"""

from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Topic(BaseModel):
    title = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


class Story(BaseModel):
    DRAFT = 'draft'
    PUBLISH = 'publish'
    ARCHIVE = 'archive'
    PENDING = 'pending'
    REJECT = 'reject'
    TRASH = 'trash'

    STATUS_CHOICES = (
        (DRAFT, 'Draft'),
        (PUBLISH, 'Publish'),
        (ARCHIVE, 'Archive'),
        (PENDING, 'Pending'),
        (REJECT, 'Reject'),
        (TRASH, 'Trash'),
    )

    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=DRAFT)
    views_count = models.PositiveBigIntegerField(default=0)
    topics = models.ManyToManyField(Topic, related_name="stories")

    @property
    def read_time(self):
        return int(len(self.content.split()) / WORDS_PER_MINUTE)


class FollowToTopic(BaseModel):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)