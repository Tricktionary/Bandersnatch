# Generated by Django 2.1.5 on 2019-02-03 00:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_auto_20190202_2333'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=400)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='game',
            name='user',
        ),
        migrations.AddField(
            model_name='game',
            name='player',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='core.Player'),
            preserve_default=False,
        ),
    ]
