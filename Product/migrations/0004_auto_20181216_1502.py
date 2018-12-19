# Generated by Django 2.0.7 on 2018-12-16 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_auto_20181215_2119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lga', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='lga',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Product.States'),
        ),
    ]
