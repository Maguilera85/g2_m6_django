# Generated by Django 3.1.5 on 2021-01-16 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='codigosnumericos',
            name='fecha',
        ),
        migrations.AlterField(
            model_name='aperturapuerta',
            name='contacto',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='aperturapuerta',
            name='opticos',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='aperturapuerta',
            name='proximidad',
            field=models.CharField(max_length=50),
        ),
    ]
