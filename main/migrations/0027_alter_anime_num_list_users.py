# Generated by Django 4.0.6 on 2022-07-14 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_alter_anime_popularity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='num_list_users',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]