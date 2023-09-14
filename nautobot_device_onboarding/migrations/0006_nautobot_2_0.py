# Generated by Django 3.2.20 on 2023-08-31 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0098_rename_data_jobresult_result'),
        ('nautobot_device_onboarding', '0005_migrate_site_to_location_part_3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onboardingtask',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='onboardingtask',
            name='device_type',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='onboardingtask',
            name='ip_address',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='onboardingtask',
            name='failed_reason',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='onboardingtask',
            unique_together={('label', 'ip_address')},
        ),
        migrations.AlterField(
            model_name='onboardingtask',
            name='status',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
