# Generated by Django 5.0.7 on 2024-08-21 23:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0001_initial'),
        ('userprofile', '0004_remove_userprofile_bio_remove_userprofile_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='qna',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qnas', to='userprofile.userprofile'),
        ),
    ]
