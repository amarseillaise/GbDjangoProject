from django.core.management.base import BaseCommand
from market.models import Customers
import random
from datetime import datetime, timedelta, date


class Command(BaseCommand):
    help = 'Create n customers'

    def add_arguments(self, parser):
        parser.add_argument('-n', type=int, help='count of customers', default=10, required=False, )

    def handle(self, *args, **kwargs):
        n = kwargs['n']
        for i in range(int(n)):
            customer = Customers(name=f'customer_{i}',
                                 email=f'example_{i}_@example.com',
                                 address=f'Grow street {i}',
                                 phone=f'+{79008223115 + i}',
                                 sign_up_date=self.get_random_date()
                                 )
            customer.save()

    @staticmethod
    def get_random_date(min_year=1970, max_year=datetime.now().year):
        start = date(min_year, 1, 1, )
        years = max_year - min_year + 1
        end = start + timedelta(days=365 * years)
        return start + (end - start) * random.random()
