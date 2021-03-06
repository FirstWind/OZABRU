# Generated by Django 3.1.7 on 2021-04-26 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('digest', '0006_auto_20210426_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='disciplina',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='participant_kod_event', to='digest.kodevent', verbose_name='вид спорта'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='vid_sporta',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='participant_vid_sporta', to='digest.vidsporta', verbose_name='вид спорта'),
        ),
        migrations.AlterField(
            model_name='referee',
            name='vid_sporta',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='referee_vid_sporta', to='digest.vidsporta', verbose_name='вид спорта'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='vid_sporta',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='trainer_vid_sporta', to='digest.vidsporta', verbose_name='вид спорта'),
        ),
    ]
