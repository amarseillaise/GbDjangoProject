from django.core.management.base import BaseCommand
from market.models import Goods
from django.utils import lorem_ipsum
from random import uniform, randint
import random
from datetime import datetime, timedelta, date


class Command(BaseCommand):
    help = 'Create n goods'

    def add_arguments(self, parser):
        parser.add_argument('-n', type=int, help='count of goods', default=10, required=False, )

    def handle(self, *args, **kwargs):
        n = kwargs['n']
        for i in range(int(n)):
            customer = Goods(title=f'good_{i}',
                             description=lorem_ipsum.words(15, common=False),
                             price=uniform(1, 100_000),
                             total_quantity=randint(0, 100),
                             add_date=self.get_random_date()
                             )
            customer.save()

    @staticmethod
    def get_random_date(min_year=1970, max_year=datetime.now().year):
        start = date(min_year, 1, 1, )
        years = max_year - min_year + 1
        end = start + timedelta(days=365 * years)
        return start + (end - start) * random.random()
