# Generated by Django 3.1.7 on 2021-04-26 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('digest', '0003_auto_20210426_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='referee',
            name='vid_sporta',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='referee_vid_sporta', to='digest.vidsporta', verbose_name='вид спорта'),
        ),
        migrations.AddField(
            model_name='trainer',
            name='vid_sporta',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='trainer_vid_sporta', to='digest.vidsporta', verbose_name='вид спорта'),
        ),
    ]
