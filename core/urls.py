# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path('auth/', include('apps.authentication.urls')),
    path('listings/', include('apps.listings.urls')),
    path('', include('apps.pages.urls')),             # UI Kits Html files 
    path('pages/', include('apps.pages.urls')),
    path('accounts/', include('apps.accounts.urls')),
    path('contacts/', include('apps.contacts.urls')),
    path('realtors/', include('apps.realtors.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
