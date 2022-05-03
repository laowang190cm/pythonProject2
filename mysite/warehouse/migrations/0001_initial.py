# Generated by Django 3.2.13 on 2022-05-01 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('deliver', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('purchase_id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('purchase_num', models.IntegerField()),
                ('purchase_time', models.DateTimeField()),
                ('purchase_price', models.FloatField(max_length=8)),
                ('deliver_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deliver.deliver')),
            ],
        ),
        migrations.CreateModel(
            name='WareHouse',
            fields=[
                ('warehouse_flow', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('left_num', models.FloatField(max_length=8)),
                ('warehouse_status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Inward',
            fields=[
                ('purchase_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='warehouse.purchase')),
                ('in_time', models.DateTimeField()),
                ('warehouse_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.warehouse')),
            ],
        ),
    ]