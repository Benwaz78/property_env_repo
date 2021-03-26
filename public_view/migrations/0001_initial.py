# Generated by Django 3.1.1 on 2021-03-26 10:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=17)),
                ('website', models.URLField(blank=True, null=True)),
                ('profile', models.ImageField(blank=True, null=True, upload_to='uploads/profile')),
                ('biography', models.TextField()),
                ('address', models.TextField()),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_name', models.CharField(max_length=200)),
                ('property_img1', models.ImageField(blank=True, null=True, upload_to='uploads/properties')),
                ('property_img2', models.ImageField(blank=True, null=True, upload_to='uploads/properties')),
                ('property_img3', models.ImageField(blank=True, null=True, upload_to='uploads/properties')),
                ('property_address', models.TextField(blank=True, null=True)),
                ('property_description', models.TextField(blank=True, null=True)),
                ('rooms', models.PositiveIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('approve', models.BooleanField(default=False)),
                ('agent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_agent', to='public_view.agents')),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_location', to='public_view.location')),
            ],
        ),
        migrations.CreateModel(
            name='ContactAgent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('agent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='public_view.agents')),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='public_view.location')),
            ],
        ),
    ]