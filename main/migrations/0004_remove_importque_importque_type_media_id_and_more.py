# Generated by Django 4.0.6 on 2022-07-27 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_animealternativetitles_table_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='importque',
            name='ImportQue_type_media_id',
        ),
        migrations.RemoveConstraint(
            model_name='useranime',
            name='UserAnime_user_anime',
        ),
        migrations.RemoveConstraint(
            model_name='usermanga',
            name='UserManga_user_manga',
        ),
        migrations.AddConstraint(
            model_name='importque',
            constraint=models.UniqueConstraint(fields=('type', 'key'), name='ImportQue_type_key'),
        ),
        migrations.AddConstraint(
            model_name='useranime',
            constraint=models.UniqueConstraint(fields=('user', 'media'), name='UserAnime_user_media'),
        ),
        migrations.AddConstraint(
            model_name='usermanga',
            constraint=models.UniqueConstraint(fields=('user', 'media'), name='UserManga_user_media'),
        ),
    ]