# Generated by Django 3.1.1 on 2021-08-06 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_auto_20201027_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='thumbnail',
            field=models.ImageField(help_text='size: 1920x1080', upload_to='blogs'),
        ),
    ]