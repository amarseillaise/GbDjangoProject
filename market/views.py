from datetime import date, timedelta
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Customers, Orders, Goods
from .forms import CustomerChoiceForm, PhotoChoiceForm

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


def all_goods(request):
    if request.method == 'GET':
        context = {}
        all_goods = []
        for good in Goods.objects.all():
            short_good = {}
            short_good['pk'] = good.pk
            short_good['title'] = good.title
            short_good['price'] = good.price
            short_good['total_quantity'] = good.total_quantity
            short_good['photo'] = good.photo
            short_good['form_photo'] = PhotoChoiceForm(pkid='upload_photo_' + str(good.pk))
            all_goods.append(short_good)
        context['all_goods'] = all_goods
        return render(request, 'all_goods.html', context)
    else:
        image = request.FILES['photo']
        to_edit_good = Goods.objects.get(id=request.POST.get('pk').split('_')[2])
        to_edit_good.photo.save(image.name, image)
        to_edit_good.save()
        return redirect('all_goods')
