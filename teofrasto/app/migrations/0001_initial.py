# Generated by Django 4.1 on 2022-08-07 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Firm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firm_name', models.CharField(max_length=255)),
                ('website', models.URLField(unique=True)),
                ('address', models.CharField(max_length=255, unique=True)),
                ('phone_number', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('construction_site', models.CharField(max_length=255, unique=True)),
                ('building_style', models.CharField(choices=[('H', 'Habitation'), ('L', 'Hospital'), ('C', 'Commerce'), ('P', 'Public Space'), ('U', 'University'), ('G', 'Government Facility')], default='H', max_length=1)),
                ('building_material', models.CharField(max_length=255)),
                ('construction_subcontract', models.CharField(max_length=255)),
                ('construction_equipement', models.CharField(max_length=255)),
                ('contract_number', models.PositiveIntegerField(unique=True)),
                ('expected_completion_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=255, unique=True)),
                ('budget', models.DecimalField(decimal_places=2, max_digits=7)),
                ('design_file', models.FileField(upload_to='')),
                ('firm', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.firm')),
            ],
        ),
        migrations.CreateModel(
            name='Architect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('computer', models.PositiveIntegerField(unique=True)),
                ('birth_date', models.DateField()),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('firm', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.firm')),
                ('project', models.ManyToManyField(to='app.project')),
            ],
        ),
    ]