# Generated by Django 4.0.4 on 2022-05-27 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('respond', '0004_alter_social_profile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social_profile',
            name='created_At',
            field=models.DateTimeField(editable=False),
        ),
        migrations.AlterField(
            model_name='social_profile',
            name='updated_At',
            field=models.DateTimeField(editable=False),
        ),
    ]
