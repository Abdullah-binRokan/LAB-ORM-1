# Generated by Django 4.2.16 on 2024-11-04 23:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_post_image_alter_post_published_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='images/default.jpg', upload_to='main/images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 4, 23, 52, 48, 278683)),
        ),
    ]
