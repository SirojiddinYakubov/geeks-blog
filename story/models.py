from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from core.models import BaseModel
from core.settings import WORDS_PER_MINUTE
from user.models import CustomUser


class Topic(BaseModel):
    title = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Story(BaseModel):
    DRAFT = 'draft'
    PUBLISHED = 'published'
    ARCHIVE = 'archive'
    PENDING = 'pending'
    REJECT = 'rejected'
    TRASH = 'trash'
    status_choices = [
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
        (ARCHIVE, 'Archive'),
        (PENDING, 'Pending'),
        (REJECT, 'Reject'),
        (TRASH, 'Trash'),
    ]
    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.CharField(max_length=10, choices=status_choices, default=DRAFT)
    views_count = models.PositiveBigIntegerField(default=0)
    topics = models.ManyToManyField(Topic, related_name="stories")

    @property
    def read_time(self):
        word_count = len(self.content.split())
        result = round(word_count / WORDS_PER_MINUTE)
        return result

    def __str__(self):
        return self.title


class FollowToTopic(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.email} follows {self.topic.title}"


class ReadStory(BaseModel):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.email} read a {self.story.title}"


class Clap(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(50)])

    def __str__(self):
        return f"Clapped by {self.user.email} with {self.count} count"


class Comment(BaseModel):
    comment = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='replies')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return f'Comment by {self.user.email} on {self.created_at}'


class FollowAuthor(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_follows')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='authored_follows')

    def __str__(self):
        return f"{self.user.email} follows {self.author.email}"
