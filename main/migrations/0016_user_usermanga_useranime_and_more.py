# Generated by Django 4.0.6 on 2022-07-14 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_animerecommendation_animerecommendation_media_recommended_media_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('info_timestamp', models.DateTimeField()),
                ('info_modified_timestamp', models.DateTimeField()),
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserManga',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=255)),
                ('score', models.PositiveSmallIntegerField()),
                ('num_episodes_watched', models.PositiveSmallIntegerField()),
                ('is_rewatching', models.BooleanField()),
                ('updated_at', models.DateTimeField()),
                ('finish_date', models.DateField()),
                ('manga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserManga_manga', to='main.manga')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserManga_user', to='main.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserAnime',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=255)),
                ('score', models.PositiveSmallIntegerField()),
                ('num_episodes_watched', models.PositiveSmallIntegerField()),
                ('is_rewatching', models.BooleanField()),
                ('updated_at', models.DateTimeField()),
                ('finish_date', models.DateField()),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserAnime_anime', to='main.anime')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserAnime_user', to='main.user')),
            ],
        ),
        migrations.AddConstraint(
            model_name='usermanga',
            constraint=models.UniqueConstraint(fields=('user', 'manga'), name='UserManga_user_manga'),
        ),
        migrations.AddConstraint(
            model_name='useranime',
            constraint=models.UniqueConstraint(fields=('user', 'anime'), name='UserAnime_user_anime'),
        ),
    ]
