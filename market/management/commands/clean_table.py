from django.core.management.base import BaseCommand
import importlib


class Command(BaseCommand):
    help = 'clean specified table'

    def add_arguments(self, parser):
        parser.add_argument('table_name', type=str, help='name of table')

    def handle(self, *args, **kwargs):
        market_module = importlib.import_module('market.models')
        try:
            table_to_clean = getattr(market_module, kwargs['table_name'])
            table_to_clean.objects.all().delete()
        except AttributeError:
            self.stdout.write('Указанной модели не существует')

