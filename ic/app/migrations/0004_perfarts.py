# Generated by Django 4.0.5 on 2022-06-19 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_painting'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerfArts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('pa_image', models.ImageField(upload_to='producting')),
            ],
        ),
    ]
