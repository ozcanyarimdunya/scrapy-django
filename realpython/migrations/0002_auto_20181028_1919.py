# Generated by Django 2.1.2 on 2018-10-28 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realpython', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutorialitem',
            old_name='link',
            new_name='url',
        ),
    ]
