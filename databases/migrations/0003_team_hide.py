# Generated by Django 3.1.1 on 2021-08-07 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databases', '0002_whyus_hide'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='hide',
            field=models.BooleanField(default=False),
        ),
    ]
