import os
import sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

#create user fake list

import random
#import user model
from first_app.models import Users

from faker import Faker

fakegenerate = Faker()

def populate(N=1):
    for data in range(N):
        faker_first_name = fakegenerate.name()
        faker_last_name = fakegenerate.name()
        faker_email = fakegenerate.email()

        user_data = Users.objects.get_or_create(first_name=faker_first_name, last_name=faker_last_name, email=faker_email)

if __name__ == '__main__':
    print('start data populating')
    populate(15)
    print('Data populating complete!')
