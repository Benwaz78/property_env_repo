# Generated by Django 3.1.1 on 2021-03-29 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public_view', '0005_property_property_type_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='prize',
            field=models.DecimalField(decimal_places=2, default=200000, max_digits=9),
            preserve_default=False,
        ),
    ]
