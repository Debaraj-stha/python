# Generated by Django 4.2 on 2023-08-14 09:05

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='multipleImageUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', django.contrib.postgres.fields.ArrayField(base_field=models.ImageField(default=[], max_length=255, null=True, upload_to='multiple_images/'), size=None)),
            ],
        ),
    ]