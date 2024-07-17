import os
import json
from django.core.management.base import BaseCommand
from django.core.exceptions import ImproperlyConfigured
from story.models import Topic


class Command(BaseCommand):
    help = 'Load initial data from topics.json into the database'

    def handle(self, *args, **kwargs):
        fixture_file = os.path.join(os.path.dirname(__file__), 'topics.json')

        if not os.path.exists(fixture_file):
            raise ImproperlyConfigured(f"{fixture_file} does not exist")

        with open(fixture_file, 'r') as file:
            topics_data = json.load(file)

        for topic_data in topics_data:
            Topic.objects.create(**topic_data)

        self.stdout.write(self.style.SUCCESS('Successfully loaded initial data'))
