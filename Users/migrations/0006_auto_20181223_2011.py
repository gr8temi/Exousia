# Generated by Django 2.0.7 on 2018-12-23 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0005_auto_20181223_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
