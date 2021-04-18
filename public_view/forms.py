from django import forms
from public_view.models import *
from django.contrib.auth.forms import User
from django.core import validators


class PropertyForm(forms.ModelForm):
	RENT = 'Rent'
	SALE = 'Sale'
	CHOOSE = ''
	OFFER_TYPE = [
	    (RENT, 'Rent'),
	    (SALE, 'Sale'),
	    (CHOOSE, 'Choose An Offer Type'),
	]
	property_name = forms.CharField(widget=forms.TextInput(
					attrs={'class':'form-control', 'placeholder':'Property Name'}
					))
	slug = forms.CharField(widget=forms.TextInput(
					attrs={'class':'form-control', 'placeholder':'Put a hyphen for your slug name'}
					))
	property_img1 = forms.ImageField(widget=forms.ClearableFileInput())
	property_img2 = forms.ImageField(widget=forms.ClearableFileInput())
	property_img3 = forms.ImageField(widget=forms.ClearableFileInput())
	prize = forms.DecimalField(widget=forms.NumberInput(
		attrs={'class':'form-control',}
		))
	property_address = forms.CharField(widget=forms.Textarea(
		attrs={'class':'form-control'}
		))
	property_description = forms.CharField(widget=forms.Textarea(
		attrs={'class':'form-control'}
		))
	rooms = forms.IntegerField(widget=forms.NumberInput(
		attrs={'class':'form-control'}
		))
	offer_type = forms.CharField(widget=forms.Select(attrs={'class':'form-control', }, choices=OFFER_TYPE), 
		)
	location_id = forms.ModelChoiceField(
		queryset=Location.objects.all(), 
		widget=forms.Select(attrs={'class': 'form-control'}),
		empty_label='Select Location'
		)
	property_type_id = forms.ModelChoiceField(
		queryset=PropertyType.objects.all(), 
		widget=forms.Select(attrs={'class': 'form-control'}),
		empty_label='Select Property Type'
		)
	approve = forms.BooleanField(widget=forms.CheckboxInput())
	botcatcher = forms.CharField(required=False, widget=forms.HiddenInput(), validators=[validators.MaxLengthValidator(0), ])

	class Meta():
		model = Property
		exclude = ('created', 'modified', 'agent_id', 'approve')

	
	