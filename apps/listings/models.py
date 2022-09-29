from .choices import (
    APPLICATION_STATUS_CHOICES,
    VIEWING_STATUS_CHOICES
)
from django.db import models
from datetime import datetime

from apps.accounts.models import (  
    ClientModel
)
from apps.realtors.models import(   
    Realtor
)



# Create your models here.

class ListingModel(models.Model):
    realtor         = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title           = models.CharField(max_length=200)
    address         = models.CharField(max_length=200)
    city            = models.CharField(max_length=100)
    state           = models.CharField(max_length=100)
    zipcode         = models.CharField(max_length=20)
    description     = models.TextField(blank=True)
    price           = models.IntegerField()
    bedrooms        = models.IntegerField()
    bathrooms       = models.DecimalField(max_digits=2, decimal_places=1)
    garage          = models.IntegerField(default=0)
    sqft            = models.IntegerField()
    lot_size        = models.DecimalField(max_digits=8, decimal_places=1)
    photo_main      = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_1         = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_2         = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_3         = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_4         = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_5         = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_6         = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    is_published    = models.BooleanField(default=True)
    list_data       = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

# APPLICATION TO PROPERTY LISTED
class PropertyApplicationModel(models.Model):
    client      = models.ForeignKey(ClientModel, on_delete=models.PROTECT)
    property    = models.ForeignKey(ListingModel, on_delete=models.PROTECT)
    message     = models.TextField(verbose_name="Application Message")
    status      = models.CharField(max_length=90,choices=APPLICATION_STATUS_CHOICES)
    response    = models.TextField()
    created_on  = models.DateTimeField(auto_now=True)
    updated_on  = models.DateTimeField(auto_now=True)
# APPLICATION TO PROPERTY LISTED

# VIEWING APPOINTMENT
class PropertyViewing(models.Model):
    application = models.ForeignKey(PropertyApplicationModel, on_delete=models.PROTECT)
    status      = models.CharField(max_length=30,choices=VIEWING_STATUS_CHOICES)
    viewing_on  = models.DateTimeField(null=False)
    created_on  = models.DateTimeField(auto_now=True)
    updated_on  = models.DateTimeField(auto_now=True)

# VIEWING APPOINTMENT
