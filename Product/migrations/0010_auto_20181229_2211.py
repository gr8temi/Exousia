# Generated by Django 2.0.7 on 2018-12-29 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0009_gender_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='gender',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='Product.Gender'),
        ),
    ]
