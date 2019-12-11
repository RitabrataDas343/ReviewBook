# Generated by Django 3.0 on 2019-12-10 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('director_name', models.CharField(max_length=200)),
                ('director_dob', models.DateField(verbose_name='Date of Birth')),
                ('director_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Publication_name', models.CharField(max_length=500)),
                ('Publication_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Star_name', models.CharField(max_length=200)),
                ('Star_dob', models.DateField(verbose_name='Date of Birth')),
                ('Star_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=400)),
                ('movie_date', models.DateField(verbose_name='date released')),
                ('movie_description', models.TextField()),
                ('movie_runningtime', models.IntegerField()),
                ('movie_totalreview', models.IntegerField()),
                ('movie_nor', models.IntegerField()),
                ('movie_image', models.ImageField(blank=True, max_length=255, null=True, upload_to='movies/')),
                ('movie_director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Director')),
                ('movie_genre', models.ManyToManyField(to='base.Genre')),
                ('movie_publication', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Publication')),
                ('movie_star', models.ManyToManyField(to='base.Star')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_name', models.CharField(max_length=400)),
                ('game_date', models.DateField(verbose_name='date released')),
                ('game_description', models.TextField()),
                ('game_size', models.DecimalField(decimal_places=2, max_digits=6)),
                ('game_totalreview', models.IntegerField()),
                ('game_nor', models.IntegerField()),
                ('game_image', models.ImageField(blank=True, max_length=255, null=True, upload_to='games/')),
                ('game_genre', models.ManyToManyField(to='base.Genre')),
                ('game_publication', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Publication')),
            ],
        ),
    ]
