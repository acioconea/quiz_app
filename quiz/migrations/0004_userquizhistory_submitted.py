# Generated by Django 4.2.7 on 2023-12-05 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_alter_response_score_remove_response_selected_answer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userquizhistory',
            name='submitted',
            field=models.BooleanField(default=False),
        ),
    ]
