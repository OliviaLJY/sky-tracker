# Generated by Django 4.2.16 on 2024-12-05 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('b13project', '0007_vote_hacky_sol'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='hacky_sol',
        ),
    ]