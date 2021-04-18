from django import forms
from public_view.models import *
from django.contrib.auth.models import User
from django.core import validators
from django.contrib.auth.forms import UserCreationForm





class RegisterForm(UserCreationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
	password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

	class Meta():
		model = User
		fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

	def save(self, commit=True):
	    user = super().save(commit=False)
	    user.username = self.cleaned_data['username']
	    user.first_name = self.cleaned_data['first_name']
	    user.last_name = self.cleaned_data['last_name']
	    user.email = self.cleaned_data['email']

	    if commit:
	        user.save()
	        return user


class LocationForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput(), validators=[validators.MaxLengthValidator(0), ])
    class Meta():
        model = Location
        fields = '__all__'


class PropertyTypeForm(forms.ModelForm):
    name = forms.CharField(label='Property Type Name', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput(), validators=[validators.MaxLengthValidator(0), ])



    def clean_name(self):
    	form_name = self.cleaned_data['name'].capitalize()
    	value_name = PropertyType.objects.filter(name=form_name).exists()
    	if value_name == True:
    		raise forms.ValidationError('Property type already exist')
    	return form_name


    class Meta():
        model = PropertyType
        fields = ('name', 'description')


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
	agent_id = forms.ModelChoiceField(
		queryset=User.objects.all(), 
		widget=forms.Select(attrs={'class': 'form-control'}),
		empty_label='Select Agent'
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
		exclude = ('created', 'modified', 'slug')




class FilterForm(forms.ModelForm):
	RENT = 'Rent'
	SALE = 'Sale'
	CHOOSE = ''
	OFFER_TYPE = [
	    (RENT, 'Rent'),
	    (SALE, 'Sale'),
	    (CHOOSE, 'Choose An Offer Type'),
	]
	property_type_id = forms.ModelChoiceField(
		queryset=PropertyType.objects.all(), 
		widget=forms.Select(attrs={'class': 'form-control d-block rounded-0'}),
		empty_label='Select Property Type'
		)
	offer_type = forms.CharField(widget=forms.Select(attrs={'class':'form-control d-block rounded-0', }, choices=OFFER_TYPE), 
		)
	location_id = forms.ModelChoiceField(
		queryset=Location.objects.all(), 
		widget=forms.Select(attrs={'class': 'form-control d-block rounded-0'}),
		empty_label='Select Location'
		)

	class Meta():
		model = Property
		fields = ('property_type_id', 'offer_type', 'location_id',)




