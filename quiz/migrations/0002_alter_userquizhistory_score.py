# Generated by Django 4.2.7 on 2023-12-05 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userquizhistory',
            name='score',
            field=models.FloatField(default=0.0),
        ),
    ]
