# Generated by Django 3.1.7 on 2021-04-25 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SportClub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название клуба', max_length=100, unique=True, verbose_name='Название')),
                ('logo', models.ImageField(blank=True, help_text='Выберите файл до 2Мб', upload_to='club', verbose_name='Логотип')),
                ('text', models.TextField(blank=True, null=True, verbose_name='О клубе')),
            ],
            options={
                'verbose_name': 'Клуб',
                'verbose_name_plural': 'Клубы',
            },
        ),
    ]
