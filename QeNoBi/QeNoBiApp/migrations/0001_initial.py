# Generated by Django 3.1.2 on 2020-11-02 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('group_id', models.IntegerField(primary_key=True, serialize=False)),
                ('period', models.DateField(max_length=30)),
                ('depth', models.IntegerField()),
                ('support', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.IntegerField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MiningGroupsExperiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frequency', models.CharField(default='1D', max_length=5)),
                ('demographics', models.CharField(default="['sex']", max_length=100)),
                ('support', models.IntegerField()),
                ('min_items', models.PositiveIntegerField()),
                ('max_items', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('sex', models.CharField(max_length=10)),
                ('age', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='QeNoBiApp.item')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='QeNoBiApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='test', max_length=30)),
                ('group_source', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sources', to='QeNoBiApp.group')),
                ('group_target', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='targets', to='QeNoBiApp.group')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='items',
            field=models.ManyToManyField(to='QeNoBiApp.Item'),
        ),
        migrations.AddField(
            model_name='group',
            name='users',
            field=models.ManyToManyField(to='QeNoBiApp.User'),
        ),
    ]
