# Generated by Django 2.0.7 on 2018-12-16 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0004_auto_20181216_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('total', models.IntegerField(default=1)),
                ('subtotal', models.IntegerField(default=1)),
                ('shipping', models.FloatField()),
                ('lga', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Product.Lga')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2018-01-01'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Product.Product'),
        ),
        migrations.AddField(
            model_name='cart',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Product.States'),
        ),
    ]
