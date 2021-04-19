# Generated by Django 3.1.7 on 2021-04-19 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20210419_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='permission',
            field=models.CharField(choices=[('Al', 'All'), ('Rd', 'Read')], default='Rd', max_length=2),
        ),
    ]
