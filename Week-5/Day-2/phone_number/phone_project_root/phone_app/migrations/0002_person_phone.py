# Generated by Django 4.2 on 2023-04-24 07:30

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('phone_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
    ]
