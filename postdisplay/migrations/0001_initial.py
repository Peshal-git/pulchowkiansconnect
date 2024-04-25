# Generated by Django 5.0.4 on 2024-04-24 18:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='postview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=50)),
                ('post_user', models.CharField(default='', max_length=20)),
                ('post_time', models.DateField(default=datetime.date.today)),
                ('post_details', models.TextField(default='')),
            ],
        ),
    ]