# Generated by Django 4.1 on 2022-08-08 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_client_budget'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client_name',
            field=models.CharField(max_length=255),
        ),
    ]
