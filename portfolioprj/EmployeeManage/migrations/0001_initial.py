# Generated by Django 3.0.3 on 2020-03-21 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('dept', models.CharField(max_length=10)),
                ('salary', models.IntegerField(max_length=10)),
                ('mail', models.EmailField(max_length=255, unique=True)),
            ],
        ),
    ]
