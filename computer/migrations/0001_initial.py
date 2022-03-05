# Generated by Django 3.1 on 2022-03-05 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComputerBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='static/img')),
            ],
        ),
        migrations.CreateModel(
            name='ComputerGeneration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gen', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ComputerSpecification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('processor_generation', models.CharField(max_length=50)),
                ('price_min', models.IntegerField()),
                ('price_max', models.IntegerField()),
                ('ram', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('computer_code', models.IntegerField(unique=True)),
                ('quantity', models.IntegerField()),
                ('unit_rate', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='computer.computerbrand')),
                ('computer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='computer.computergeneration')),
                ('computer_specification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='computer.computerspecification')),
            ],
        ),
    ]