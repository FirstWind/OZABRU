# Generated by Django 3.1.7 on 2021-04-26 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('digest', '0004_auto_20210426_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='vid_sporta',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='participant_vid_sporta', to='digest.vidsporta', verbose_name='вид спорта'),
        ),
        migrations.AlterField(
            model_name='referee',
            name='vid_sporta',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='referee_vid_sporta', to='digest.vidsporta', verbose_name='вид спорта'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='vid_sporta',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trainer_vid_sporta', to='digest.vidsporta', verbose_name='вид спорта'),
        ),
    ]