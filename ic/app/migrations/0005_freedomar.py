# Generated by Django 4.0.5 on 2022-06-19 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_perfarts'),
    ]

    operations = [
        migrations.CreateModel(
            name='freedomar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('R', 'Rare Books'), ('I', 'Images'), ('N', 'Newspaper Clippings')], max_length=2)),
                ('fr_image', models.ImageField(upload_to='producting')),
            ],
        ),
    ]
