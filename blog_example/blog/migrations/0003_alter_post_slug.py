# Generated by Django 5.1.6 on 2025-03-07 08:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_remove_post_blog_post_publish_c4286e_idx_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(max_length=250, unique_for_date="publish"),
        ),
    ]
