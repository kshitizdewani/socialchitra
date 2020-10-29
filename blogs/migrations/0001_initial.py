# Generated by Django 3.1.1 on 2020-10-26 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=50)),
                ('created', models.DateField(auto_now_add=True)),
                ('body', models.CharField(max_length=2000)),
                ('thumbnail', models.ImageField(upload_to='media')),
            ],
        ),
    ]
