# Generated by Django 5.2.2 on 2025-06-08 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land_management', '0003_approval_date_created_landmapping_date_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landregistration',
            name='size_unit',
            field=models.CharField(blank=True, default='sqm', max_length=10),
        ),
    ]
