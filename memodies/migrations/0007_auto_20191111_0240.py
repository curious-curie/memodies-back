# Generated by Django 2.1.7 on 2019-11-11 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memodies', '0006_post_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='owner',
        ),
    ]
