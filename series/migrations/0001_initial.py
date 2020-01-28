# Generated by Django 3.0 on 2020-01-28 14:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import series.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('episode_name', models.CharField(max_length=400)),
                ('episode_number', models.IntegerField()),
                ('season_number', models.IntegerField(default=1)),
                ('description', models.TextField(blank=True)),
                ('release_date', models.DateField(verbose_name='Edisode Release Date')),
                ('running_time', models.DurationField()),
                ('totalreview', models.IntegerField(default=0)),
                ('totalrating', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to=series.models.upload_location_episode)),
                ('avgrating', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('director', models.ManyToManyField(to='base.Director')),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('release_date', models.DateField(verbose_name='First Episode Released')),
                ('description', models.TextField(blank=True)),
                ('running_time', models.DurationField()),
                ('total_episode', models.IntegerField(default=1)),
                ('total_season', models.IntegerField(default=1)),
                ('total_review', models.IntegerField(default=0)),
                ('nor', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to=series.models.upload_location_series)),
                ('avg_review', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('director', models.ManyToManyField(to='base.Director')),
                ('genre', models.ManyToManyField(to='base.Genre')),
                ('publication', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Publication')),
                ('star', models.ManyToManyField(to='base.Star')),
            ],
        ),
        migrations.CreateModel(
            name='EpisodeReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('body', models.TextField(max_length=5000)),
                ('rating', models.IntegerField(default=1)),
                ('date_published', models.DateTimeField(auto_now_add=True, verbose_name='Date Reviewed')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='series.Episode')),
            ],
        ),
        migrations.AddField(
            model_name='episode',
            name='show_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='series.Series'),
        ),
    ]
