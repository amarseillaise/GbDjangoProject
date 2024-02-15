from datetime import date, timedelta
from django.shortcuts import render
from .models import Customers, Orders, Goods
from .forms import CustomerChoiceForm

# Create your views here.


def index(request):
    context = {"title": "Главная", 'customer_selector': CustomerChoiceForm()}
    return render(request, 'index.html', context)


def customer_statistic(request):
    def get_orders_by_date_range(all_orders, delta):
        ranged_orders = all_orders.filter(add_date__range=[date.today() - timedelta(days=delta), date.today()])
        goods = [{'title': good['title'], 'add_date': order.add_date} for order in ranged_orders for good in order.goods.values()]
        return goods

    if request.method == 'POST':
        context = {}
        c_id = request.POST.get('customer')
        customer = Customers.objects.get(pk=c_id)
        all_customers_orders = Orders.objects.filter(user_id=c_id)
        context['customer'] = customer
        context['week_orders'] = get_orders_by_date_range(all_customers_orders, 7)
        context['month_orders'] = get_orders_by_date_range(all_customers_orders, 31)
        context['year_orders'] = get_orders_by_date_range(all_customers_orders, 365)
        print(context['week_orders'])
        print(context['month_orders'])
        print(context['year_orders'])
        return render(request, 'statistic.html', context)

