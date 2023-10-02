from typing import Any
from django import forms
from .models import ListingModel, PropertyApplicationModel
from apps.realtors.models import Realtor

class CreateRentalListingForm(forms.ModelForm):
    class Meta:
        model = ListingModel
        # fields = '__all__'
        fields = [
            'photo_main',
            'title',
            'description',
            'address_line_one',
            'address_line_two',
            'city',
            'state',
            'zipcode',
            'price',
            'bedrooms',
            'bathrooms',
            'garage',
            'sqft',
            'realtor'
        ]
        widgets = {
            'photo_main':forms.FileInput(attrs={'class': "form-control" }),
            'title': forms.TextInput(attrs={'class': "form-control","placeholder":"Title"}),
            'address_line_one':forms.TextInput(attrs={'class': "form-control","placeholder":"Address Line One" }),
            'address_line_two':forms.TextInput(attrs={'class': "form-control","placeholder":"Address Line Two" }),
            'city': forms.TextInput(attrs={'class': "form-control","placeholder":"City" }),
            'state': forms.TextInput(attrs={'class': "form-control","placeholder":"State" }),
            'zipcode': forms.TextInput(attrs={'class': "form-control" ,"placeholder":"Zip Code" }),
            'description': forms.Textarea(attrs={'class': "form-control" ,"placeholder":"Listing Description" }),
            'price': forms.TextInput(attrs={'class': "form-control" ,"placeholder":"Price" }),
            'bedrooms': forms.NumberInput(attrs={'class': "form-control" ,"placeholder":"No. Bedrooms" }),
            'bathrooms': forms.NumberInput(attrs={'class': "form-control" ,"placeholder":"No. Bathrooms" }),
            'garage': forms.CheckboxInput(attrs={'class': "form-control" }),
            'sqft': forms.NumberInput(attrs={'class': "form-control" ,"placeholder":"Property Ares Sq Ft" }),
            'realtor': forms.Select(choices=Realtor.objects.filter(is_enabled=True),attrs={'class': "form-control" ,"placeholder":"Select a Realtor" })
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""
            field.required = False

    def save(self, commit=True):
        m = super(CreateRentalListingForm, self).save(commit=False)
        # do custom stuff
        if commit:
            m.save()
        return m
    
class CreateListingApplicationForm(forms.ModelForm):
    class Meta:
        model = PropertyApplicationModel
        # fields = '__all__'
        fields = [
            'phone_number',
            'message',
            'move_in_date',
            'occupants',
        ]
        widgets = {
            'occupants': forms.NumberInput(attrs={'class': "filter-widget " ,"placeholder":"No. of Occupants" }),
            'phone_number': forms.TextInput(attrs={'class': "filter-widget " ,"placeholder":"Phone Number"}),
            'message': forms.Textarea(attrs={'class': "filter-widget " ,"placeholder":"Your message",'name':'booking_msg','id':"booking_msg"}),
            'move_in_date': forms.DateInput(attrs={'placeholder':'Move in date'})
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""
            field.required = False
        self.fields['move_in_date'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 
                'placeholder': 'Move in Date',
                'class': 'filter-widget'
                }
            )
    def save(self, commit, client, property):
        application = super(CreateListingApplicationForm,self).save(commit)
        application.client = client
        application.property = property
        application.status = 'open'
        application.save()
        return application
    