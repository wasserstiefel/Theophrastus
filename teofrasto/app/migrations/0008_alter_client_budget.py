# Generated by Django 4.1 on 2022-08-08 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_client_design_file_remove_client_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='budget',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
    ]