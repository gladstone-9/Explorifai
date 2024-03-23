# Generated by Django 5.0.3 on 2024-03-23 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('description', models.CharField(default='', max_length=400)),
                ('lat', models.DecimalField(decimal_places=25, max_digits=25)),
                ('long', models.DecimalField(decimal_places=25, max_digits=25)),
            ],
        ),
    ]
