# Generated by Django 5.0.6 on 2024-07-17 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
