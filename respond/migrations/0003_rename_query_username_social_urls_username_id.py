# Generated by Django 4.0.4 on 2022-05-22 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('respond', '0002_users_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='social_urls',
            old_name='query_username',
            new_name='username_id',
        ),
    ]
