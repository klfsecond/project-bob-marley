from django.contrib import admin

# Register your models here.
from .models import (
    ClientModel,

)

class ClientAdmin(admin.ModelAdmin):
    list_display        = ('id', 'email', 'created_at','email_verified','is_enabled')
    list_display_links  = ('id', 'email')
    list_filter         = ('id', 'email')
    list_editable       = ('is_enabled',)
    search_fields       = ('id', 'email','firstname','lastname','created_at','email_verified','is_enabled')


admin.site.register(ClientModel,ClientAdmin)
