# Generated by Django 4.0.4 on 2022-04-14 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thinker', models.CharField(max_length=200)),
                ('text', models.TextField()),
            ],
        ),
    ]
