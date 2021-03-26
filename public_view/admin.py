from django.contrib import admin
from public_view.models import *
admin.site.site_header='Property Website'

# Register your models here.
admin.site.register(Agents)
admin.site.register(PropertyType)
admin.site.register(Location)
admin.site.register(ContactAgent)


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('property_name',)}
