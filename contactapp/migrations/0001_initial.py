# Generated by Django 5.1.1 on 2024-09-20 04:49

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactNum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.TextField(max_length=50)),
                ('lestname', models.TextField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=12)),
                ('description', tinymce.models.HTMLField()),
            ],
        ),
    ]
