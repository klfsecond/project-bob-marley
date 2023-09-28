from django import forms
from .models import ListingModel

class CreateRentalListing(forms.ModelForm):
    class Meta:
        model = ListingModel
        fields = '__all__'