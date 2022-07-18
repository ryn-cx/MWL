# Generated by Django 4.0.6 on 2022-07-14 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_remove_animerelatedanime_related_and_more'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='animerecommendation',
            constraint=models.UniqueConstraint(fields=('media', 'recommended_media'), name='AnimeRecommendation_media_recommended_media'),
        ),
        migrations.AddConstraint(
            model_name='animerelatedanime',
            constraint=models.UniqueConstraint(fields=('media', 'related_media'), name='AnimeRelatedAnime_media_related_media'),
        ),
        migrations.AddConstraint(
            model_name='animerelatedmanga',
            constraint=models.UniqueConstraint(fields=('media', 'related_media'), name='AnimeRelatedManga_media_related_media'),
        ),
        migrations.AddConstraint(
            model_name='mangarecommendation',
            constraint=models.UniqueConstraint(fields=('media', 'recommended_media'), name='MangaRecommendation_media_recommended_media'),
        ),
        migrations.AddConstraint(
            model_name='mangarelatedanime',
            constraint=models.UniqueConstraint(fields=('media', 'related_media'), name='MangaRelatedAnime_media_related_media'),
        ),
        migrations.AddConstraint(
            model_name='mangarelatedmanga',
            constraint=models.UniqueConstraint(fields=('media', 'related_media'), name='MangaRelatedManga_media_related_media'),
        ),
    ]
