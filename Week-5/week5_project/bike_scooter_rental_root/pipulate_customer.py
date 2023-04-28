import os
import django
from faker import Faker
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bike_scooter_rental.settings')
django.setup()
from bsrent_app.models import Customer

fake = Faker()


for i in range(100):
    first_name  = fake.first_name(), 
    last_name   = fake.last_name(),
    email       = fake.email()
    number      = fake.phone_number()
    address     = fake.street_address()
    city        = fake.city()
    country     = fake.country()
    print(first_name,last_name)
    new_customer = Customer(
                        first_name = first_name[0],  
                        last_name = last_name[0],
                        email = email,  
                        number = number, 
                        address = address,
                        city = city,
                        country    = country
                        )


    # new_rental = Rentals(
    #             title='POPULATED',
    #             url='https://media.giphy.com/media/SggILpMXO7Xt6/giphy.gif',
    #             uploader_name='Yossi')
    
    new_customer.save()