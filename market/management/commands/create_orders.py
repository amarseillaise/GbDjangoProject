from django.core.management.base import BaseCommand
from market.models import Orders, Customers, Goods
from random import randint, choice
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
            order = Orders.objects.create(user=choice(Customers.objects.all()),
                                          total_price=total_price,
                                          add_date=self.get_random_date()
                                          )
            order.goods.set(goods)

    @staticmethod
    def get_random_date(min_date=datetime(2023, 1, 1).date(), max_date=datetime.now().date()):
        different = timedelta(days=(max_date - min_date).days)
        return min_date + different * random.random()

    @staticmethod
    def get_goods_list_and_total_price():
        goods = {choice(Goods.objects.all()) for _ in range(randint(1, 10))}
        total_price = sum([price.price for price in goods])
        return total_price, goods
