# Generated by Django 4.1 on 2022-08-08 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_project_contract_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='architect',
            name='computer',
            field=models.CharField(default='00000', max_length=14, unique=True),
        ),
    ]