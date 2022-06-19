# Generated by Django 4.0.5 on 2022-06-19 05:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_musicali'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musicali',
            name='type',
        ),
        migrations.AddField(
            model_name='musicali',
            name='category',
            field=models.CharField(choices=[('A', ' Avanaddha Vadya'), ('T', 'Tat Vadya'), ('G', 'Ghan Vadya'), ('S', 'Sushir Vadya')], default=django.utils.timezone.now, max_length=4),
            preserve_default=False,
        ),
    ]