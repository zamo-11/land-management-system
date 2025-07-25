# Generated by Django 5.2 on 2025-06-08 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land_management', '0004_alter_landregistration_size_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='approval',
            name='rejection_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='approval',
            name='rejection_reason',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='approval',
            name='return_step',
            field=models.CharField(blank=True, choices=[('registration', 'Land Registration'), ('survey_payment', 'Survey Payment'), ('land_survey', 'Land Survey'), ('tax_payment', 'Tax Payment'), ('land_mapping', 'Land Mapping')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='approval',
            name='returned_by',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='approval',
            name='deputy_mayor_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected'), ('returned', 'Returned for Correction')], default='pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='approval',
            name='director_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected'), ('returned', 'Returned for Correction')], default='pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='approval',
            name='mayor_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected'), ('returned', 'Returned for Correction')], default='pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='approval',
            name='secretary_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected'), ('returned', 'Returned for Correction')], default='pending', max_length=20),
        ),
    ]
