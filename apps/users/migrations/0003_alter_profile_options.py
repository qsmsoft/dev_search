# Generated by Django 4.1.7 on 2023-04-06 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_message'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['created']},
        ),
    ]
