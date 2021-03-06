# Generated by Django 3.1.7 on 2021-04-25 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('digest', '0001_initial'),
        ('club', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sportclub',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='club_address', to='digest.location', verbose_name='адрес клуба'),
        ),
        migrations.AddField(
            model_name='sportclub',
            name='name_sorev',
            field=models.ManyToManyField(related_name='club_sorev', to='digest.VidSporta', verbose_name='Спортивная специализация'),
        ),
        migrations.AddField(
            model_name='sportclub',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='club_human', to='digest.human', verbose_name='владелец клуба'),
        ),
        migrations.AddField(
            model_name='sportclub',
            name='participant',
            field=models.ManyToManyField(related_name='participant_club', to='digest.Human', verbose_name='Участники клуба'),
        ),
    ]
