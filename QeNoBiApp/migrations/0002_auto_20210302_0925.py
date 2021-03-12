# Generated by Django 3.1.2 on 2021-03-02 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('QeNoBiApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataSetDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SankeyExperiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataset', models.CharField(max_length=100)),
                ('date_min', models.DateField(max_length=100)),
                ('date_max', models.DateField(max_length=100)),
                ('demographics', models.CharField(max_length=100)),
                ('product', models.CharField(max_length=100)),
                ('time_granularity', models.CharField(max_length=100)),
                ('support', models.IntegerField()),
                ('products_min', models.IntegerField()),
                ('max_products', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=100)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='QeNoBiApp.datasetdescription')),
            ],
        ),
        migrations.AddField(
            model_name='datasetdescription',
            name='customers_properties',
            field=models.ManyToManyField(related_name='dataset_customers', to='QeNoBiApp.Property'),
        ),
        migrations.AddField(
            model_name='datasetdescription',
            name='items_properties',
            field=models.ManyToManyField(related_name='dataset_items', to='QeNoBiApp.Property'),
        ),
    ]