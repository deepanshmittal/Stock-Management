# Generated by Django 4.1.3 on 2022-12-12 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_dyer_finisher_officestock_finishingstock_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=10, unique=True)),
            ],
        ),
    ]
