# Generated by Django 3.2.13 on 2022-11-23 02:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('sub_title', models.TextField()),
                ('char', models.TextField()),
                ('genres', models.TextField()),
                ('img', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mbti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('type', models.TextField()),
                ('choice1', models.TextField()),
                ('choice2', models.TextField()),
                ('picture1', models.TextField()),
                ('picture2', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('popularity', models.FloatField()),
                ('vote_average', models.FloatField()),
                ('vote_count', models.IntegerField()),
                ('overview', models.TextField()),
                ('poster_path', models.CharField(max_length=200)),
                ('genres', models.ManyToManyField(to='movies.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
