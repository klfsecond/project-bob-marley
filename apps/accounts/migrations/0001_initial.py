# Generated by Django 3.2.11 on 2022-09-29 19:50

import apps.accounts.model_fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientModel',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', apps.accounts.model_fields.LowercaseEmailField(max_length=254, unique=True, verbose_name='Email')),
                ('system_id', models.IntegerField(default=1)),
                ('username', models.CharField(max_length=60)),
                ('firstname', models.CharField(blank=True, max_length=30, null=True)),
                ('lastname', models.CharField(blank=True, max_length=30, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('email_verified', models.BooleanField(default=False)),
                ('is_enabled', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
