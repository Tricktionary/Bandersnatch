# Generated by Django 2.1.5 on 2019-02-03 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20190203_0058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='player',
            new_name='user',
        ),
    ]
