# Generated by Django 5.0.7 on 2024-08-22 00:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_rename_user_id_post_author'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='post',
            table='posts',
        ),
    ]
