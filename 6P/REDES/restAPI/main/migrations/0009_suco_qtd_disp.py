# Generated by Django 3.2.5 on 2021-07-27 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_suco_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='suco',
            name='qtd_disp',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
