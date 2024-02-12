from django.core.management.base import BaseCommand
from market.models import Customers


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
                                 )
            customer.save()
