# Generated by Django 4.0.4 on 2022-06-01 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('respond', '0004_alter_users_extended_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social_profile',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='social_profile',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]