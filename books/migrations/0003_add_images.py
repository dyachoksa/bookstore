# Generated by Django 3.1.7 on 2021-02-23 18:02

import books.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_add_timestamps_to_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='photo',
            field=models.ImageField(blank=True, max_length=300, null=True, upload_to='authors/%Y'),
        ),
        migrations.AddField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(blank=True, max_length=300, null=True, upload_to=books.models.get_image_path),
        ),
    ]
