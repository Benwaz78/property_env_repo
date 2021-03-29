from public_view.models import *


def property_type(request):
    prop = PropertyType.objects.all()
    return {'pro':prop}