# Generated by Django 4.0.6 on 2022-07-27 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_animerecs_media_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='start_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='manga',
            name='start_date',
            field=models.DateField(null=True),
        ),
    ]
