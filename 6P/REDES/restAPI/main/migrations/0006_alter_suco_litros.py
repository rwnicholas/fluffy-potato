# Generated by Django 3.2.5 on 2021-07-27 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_suco_litros'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suco',
            name='litros',
            field=models.FloatField(),
        ),
    ]
