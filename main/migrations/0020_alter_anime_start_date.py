# Generated by Django 4.0.6 on 2022-07-14 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='start_date',
            field=models.DateField(null=True),
        ),
    ]