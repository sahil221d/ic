# Generated by Django 4.0.5 on 2022-06-19 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_freedomar_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freedomar',
            name='category',
            field=models.CharField(choices=[('R', 'Rare Books'), ('I', 'Images'), ('N', 'Newspaper Clippings')], max_length=4),
        ),
    ]
