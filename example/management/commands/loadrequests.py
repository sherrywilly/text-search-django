import requests
from django.core.management.base import BaseCommand,CommandError
from example.models import User

class Command(BaseCommand):

    def handle(self, *args, **options) :

        
        for i in range(1,10,1):
            url= f"https://reqres.in/api/users?page={i}"
            data = requests.get(url)
            jsondata = data.json()['data']
            for x in jsondata:
                User.objects.create(email = x['email'],fname = x['first_name'],lname=x['last_name'])
        return True
            



