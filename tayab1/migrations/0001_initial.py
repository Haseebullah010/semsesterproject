# Generated by Django 3.2.9 on 2021-11-29 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('password1', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=100)),
                ('mail', models.EmailField(max_length=254)),
                ('password1', models.CharField(max_length=100)),
            ],
        ),
    ]
