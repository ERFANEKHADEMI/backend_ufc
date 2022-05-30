# Generated by Django 4.0.4 on 2022-05-29 19:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='urlOption',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('urlOptionName', models.CharField(max_length=100)),
                ('urlOptionUrl', models.URLField(blank=True)),
                ('urlOptionColor', models.CharField(blank=True, max_length=100, null=True)),
                ('svg_logo', models.FileField(blank=True, null=True, upload_to='logos')),
                ('logo_url', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users_extended',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('phone', models.CharField(blank=True, max_length=24, null=True, unique=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('job', models.CharField(blank=True, max_length=100, null=True)),
                ('created_At', models.DateTimeField(auto_now=True)),
                ('updated_At', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='social_profile',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('socialProfileUsername', models.CharField(blank=True, max_length=15, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('urlOptionId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='respond.urloption')),
                ('userurl_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
