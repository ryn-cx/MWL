# Generated by Django 4.0.6 on 2022-07-14 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_alter_anime_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='start_season_year',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
