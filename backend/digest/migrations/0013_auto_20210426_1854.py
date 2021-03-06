# Generated by Django 3.1.7 on 2021-04-26 09:54

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('sports_category', '0005_delete_participantcategory'),
        ('digest', '0012_auto_20210426_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='human',
            name='city',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='human', to='digest.city', verbose_name='город(регион)'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='participant_category', to='sports_category.category', verbose_name='разряд'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='disciplina',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='participant_kod_event', to='digest.kodevent', verbose_name='вид спорта'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='vid_sporta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='participant_vid_sporta', to='digest.vidsporta', verbose_name='вид спорта'),
        ),
        migrations.AlterField(
            model_name='referee',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='digest.city', verbose_name='город(регион)'),
        ),
        migrations.AlterField(
            model_name='referee',
            name='vid_sporta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='referee_vid_sporta', to='digest.vidsporta', verbose_name='вид спорта'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='description',
            field=models.TextField(default='', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='vid_sporta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trainer_vid_sporta', to='digest.vidsporta', verbose_name='вид спорта'),
        ),
        migrations.AlterField(
            model_name='userphone',
            name='number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True, verbose_name='№ Телефона'),
        ),
    ]
