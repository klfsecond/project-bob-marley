# Generated by Django 3.2.11 on 2023-10-01 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0010_propertyapplicationmodel_move_in_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertyapplicationmodel',
            name='move_in_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
