# Generated by Django 4.0 on 2021-12-17 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long', models.URLField(max_length=250)),
                ('short', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
