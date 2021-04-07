from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
# Create your models here.

class MoreProfile(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Agent')
    phone = models.CharField(max_length=17)
    website = models.URLField(blank=True, null=True)
    profile = models.FileField(blank=True, null=True, upload_to='uploads/profile')
    biography = models.TextField()
    address = models.TextField()

    class Meta():
        verbose_name_plural='User Profile'

class Location(models.Model):
    name =models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name


class PropertyType(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Team(models.Model):
    team_name = models.CharField(max_length=150)
    profile = models.FileField(blank=True, null=True, upload_to='uploads/')
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.team_name

    class Meta():
        verbose_name_plural = 'Team'

class Property(models.Model):
    RENT = 'Rent'
    SALE = 'Sale'
    CHOOSE = ''
    OFFER_TYPE = [
        (RENT, 'Rent'),
        (SALE, 'Sale'),
        (CHOOSE, 'Choose An Offer Type'),
    ]
    property_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    property_img1 = models.FileField(blank=True, null=True, verbose_name='Property Image 1', upload_to='uploads/properties')
    property_img2 = models.FileField(blank=True, null=True, verbose_name='Property Image 2', upload_to='uploads/properties')
    property_img3 = models.FileField(
        blank=True, null=True, verbose_name='Property Image 3', upload_to='uploads/properties')
    prize = models.DecimalField(max_digits=9, decimal_places=2)
    property_address = models.TextField(blank=True, null=True)
    property_description = models.TextField(blank=True, null=True)
    rooms = models.PositiveIntegerField()
    offer_type = models.CharField(max_length=10, choices=OFFER_TYPE, default=CHOOSE)
    location_id = models.ForeignKey(Location, related_name='property_location', on_delete=models.CASCADE)
    agent_id = models.ForeignKey(User, related_name='property_agent', on_delete=models.CASCADE)
    property_type_id = models.ForeignKey(
        PropertyType, related_name='property_type', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    approve = models.BooleanField(default=False)

    def __str__(self):
        return self.property_name
    
    def img_url1(self):
        if self.property_img1.url:
            return self.property_img1.url
        else:
            return '/static/public/images/img_1.jpg'
    
    def img_url2(self):
        if self.property_img2.url:
            return self.property_img2.url
        else:
            return '/static/public/images/img_1.jpg'

    def img_url3(self):
        if self.property_img3.url:
            return self.property_img3.url
        else:
            return '/static/public/images/img_1.jpg'

    class Meta():
        verbose_name_plural = 'Property'

    def get_property_url(self):
        return reverse("public_view:property_details", kwargs={
            'slug': self.slug,
            'category_id':self.property_type_id.id,
            'prop_id':self.id
        })

    def approve_property(self):
        self.approve = True
        self.save()
    
    def disapprove_property(self):
        self.approve = False
        self.save()

class ContactAgent(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    agent_id = models.ForeignKey(User, on_delete=models.CASCADE)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)





