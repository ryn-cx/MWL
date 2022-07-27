# Generated by Django 4.0.6 on 2022-07-27 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rename_animerecommendation_animerecs_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animerecs',
            name='media',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='AnimeRecs_Anime_media', to='main.anime'),
        ),
        migrations.AlterField(
            model_name='animerecs',
            name='recommended_media',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='AnimeRecs_Anime_recommended_media', to='main.anime'),
        ),
        migrations.AlterField(
            model_name='mangarecs',
            name='media',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='MangaRecs_Manga_media', to='main.manga'),
        ),
        migrations.AlterField(
            model_name='mangarecs',
            name='recommended_media',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='MangaRecs_Manga_recommended_media', to='main.manga'),
        ),
        migrations.AlterField(
            model_name='mangarelatedmanga',
            name='media',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='MangaRelatedManga_Manga_media', to='main.manga'),
        ),
        migrations.AlterField(
            model_name='mangarelatedmanga',
            name='related_media',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='MangaRelatedManga_Manga_related_media', to='main.manga'),
        ),
        migrations.AlterField(
            model_name='useranime',
            name='media',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserAnime_Anime_media', to='main.anime'),
        ),
        migrations.AlterField(
            model_name='useranime',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserAnime_User_user', to='main.user'),
        ),
        migrations.AlterField(
            model_name='usermanga',
            name='media',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserManga_Manga_media', to='main.manga'),
        ),
        migrations.AlterField(
            model_name='usermanga',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserManga_User_user', to='main.user'),
        ),
    ]