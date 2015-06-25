# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import pinax.pages.models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(upload_to=pinax.pages.models.generate_filename)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('path', models.CharField(unique=True, max_length=100)),
                ('body', models.TextField()),
                ('body_html', models.TextField(editable=False, blank=True)),
                ('status', models.IntegerField(default=2, choices=[(1, 'Draft'), (2, 'Public')])),
                ('publish_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
    ]
