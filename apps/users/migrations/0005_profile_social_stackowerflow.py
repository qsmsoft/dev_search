# Generated by Django 4.1.7 on 2023-04-01 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='social_stackowerflow',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
