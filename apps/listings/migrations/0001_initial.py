# Generated by Django 3.2.11 on 2022-09-29 19:50

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListingModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.DecimalField(decimal_places=1, max_digits=2)),
                ('garage', models.IntegerField(default=0)),
                ('sqft', models.IntegerField()),
                ('lot_size', models.DecimalField(decimal_places=1, max_digits=8)),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('photo_6', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('is_published', models.BooleanField(default=True)),
                ('list_data', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.realtor')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyApplicationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='Application Message')),
                ('status', models.CharField(choices=[('open', 'Open'), ('scheduled', 'Scheduled'), ('rejected', 'Rejected'), ('closed', 'Closed')], max_length=90)),
                ('response', models.TextField()),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='listings.listingmodel')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyViewing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('open', 'Open'), ('rescheduled', 'Re-Scheduled'), ('canceled', 'canceled')], max_length=30)),
                ('viewing_on', models.DateTimeField()),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='listings.propertyapplicationmodel')),
            ],
        ),
    ]
