# Generated by Django 2.2.5 on 2019-11-11 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20191111_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showing',
            name='showtime',
            field=models.TextField(),
        ),
    ]
