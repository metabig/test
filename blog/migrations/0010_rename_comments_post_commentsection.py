# Generated by Django 3.2.14 on 2022-07-11 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20220711_1201'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='comments',
            new_name='commentSection',
        ),
    ]