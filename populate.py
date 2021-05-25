import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','modelsproj.settings')
import django
django.setup()


from  demolapp.models import *
from faker import Faker
from random import *
faker=Faker()
def populate(n):
    for i in range(n):
        feno=randint(1001,9999)
        fename=faker.name()
        fesalary=randint(100000,999999)
        feaddr=faker.city()
        emp_record=Employee.objects.get_or_create(eno=feno,ename=fename,esalary=fesalary,eaddr=feaddr)
populate(30)
