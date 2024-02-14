from django.core.management.base import BaseCommand
from market.models import Orders, Customers, Goods
from django.utils import lorem_ipsum
from random import uniform, randint, choice
import random
from datetime import datetime, timedelta, date


class Command(BaseCommand):
    help = 'Create n orders'

    def add_arguments(self, parser):
        parser.add_argument('-n', type=int, help='count of orders', default=10, required=False, )

    def handle(self, *args, **kwargs):
        n = kwargs['n']
        for i in range(int(n)):
            total_price, goods = self.get_goods_list_and_total_price()
            order = Orders.objects.create(user=self.get_random_user(),
                                          total_price=total_price,
                                          add_date=self.get_random_date()
                                          )
            order.goods.set(goods)

    @staticmethod
    def get_random_date(min_year=1970, max_year=datetime.now().year):
        start = date(min_year, 1, 1, )
        years = max_year - min_year + 1
        end = start + timedelta(days=365 * years)
        return start + (end - start) * random.random()

    @staticmethod
    def get_random_user():
        user_id = randint(1, len(Customers.objects.all()) + 1)
        return Customers.objects.filter(id=user_id).first()

    @staticmethod
    def get_goods_list_and_total_price():
        goods = [choice(Goods.objects.all()) for _ in range(randint(1, 10))]
        total_price = sum([price.price for price in goods])
        return total_price, goods
