# Generated by Django 4.0.6 on 2022-07-15 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_alter_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='anime_count',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='manga_count',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]