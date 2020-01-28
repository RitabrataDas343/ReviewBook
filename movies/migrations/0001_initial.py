# Generated by Django 3.0 on 2020-01-28 14:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import movies.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('releasedate', models.DateField(verbose_name='date released')),
                ('description', models.TextField(blank=True)),
                ('runningtime', models.DurationField()),
                ('totalreview', models.IntegerField(default=0)),
                ('totalrating', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to=movies.models.upload_location)),
                ('avgrating', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Director')),
                ('genre', models.ManyToManyField(to='base.Genre')),
                ('publication', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Publication')),
                ('stars', models.ManyToManyField(to='base.Star')),
            ],
        ),
        migrations.CreateModel(
            name='MovieReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('body', models.TextField(max_length=5000)),
                ('rating', models.IntegerField()),
                ('date_published', models.DateTimeField(auto_now_add=True, verbose_name='Date Reviewed')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='MovieFollow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movie')),
            ],
        ),
    ]
