# Generated by Django 3.2.11 on 2023-09-30 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='realtor',
            name='is_enabled',
            field=models.BooleanField(default=False),
        ),
    ]