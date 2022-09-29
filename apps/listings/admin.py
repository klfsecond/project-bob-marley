from django.contrib import admin

# Register your models here.

from apps.listings.models import (
    ListingModel,
    PropertyApplicationModel,
    PropertyViewing
)


class ListingAdmin(admin.ModelAdmin):
    list_display        = ('id', 'title', 'is_published','price', 'list_data', 'realtor')
    list_display_links  = ('id', 'title')
    list_filter         = ('realtor',)
    list_editable       = ('is_published',)
    search_fields       = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    list_per_page       = 25


admin.site.register(ListingModel, ListingAdmin)
admin.site.register(PropertyApplicationModel)
admin.site.register(PropertyViewing)

