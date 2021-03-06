# Generated by Django 3.1.7 on 2021-04-26 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('digest', '0014_auto_20210426_2111'),
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(blank=True, help_text='название события', max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='event',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='digest.city', verbose_name='Город(район)'),
        ),
        migrations.AlterField(
            model_name='event',
            name='short_description',
            field=models.CharField(blank=True, default='', help_text='краткое описание (анонс 300симв)', max_length=300, verbose_name='Текст'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='vid',
            field=models.ForeignKey(blank=True, help_text='ориентирование,трейл...', null=True, on_delete=django.db.models.deletion.CASCADE, to='digest.vidsporta', verbose_name='Вид события'),
        ),
        migrations.AlterField(
            model_name='programevent',
            name='name',
            field=models.CharField(blank=True, default='', help_text='судейская, соревнование, экскурсия...', max_length=80, verbose_name='Название'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='programevent',
            name='program_text',
            field=models.TextField(blank=True, default='', verbose_name='Текст'),
            preserve_default=False,
        ),
    ]
