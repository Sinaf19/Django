# Generated by Django 5.1.6 on 2025-03-13 12:44
from django.contrib.postgres.operations import TrigramExtension
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0005_post_tags"),
    ]

    operations = [
        TrigramExtension(),
    ]
