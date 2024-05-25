from django.shortcuts import render
from .models import Order
from .forms import OrderForm
from cms.models import Cms_slider
from price.models import PriceCard, PriceTable
from telebot.sendmessage import sendTelegram
# Create your views here.
def indexPage(request):
    slider = Cms_slider.objects.all()
    price_table = PriceTable.objects.all()
    price_card = PriceCard.objects.all()
    orders = Order.objects.all()
    form = OrderForm()
    context = {'slider': slider, 'price_table': price_table, 'price_card': price_card, 'orders': orders, 'form': form}
    return render(request, "./index.html", context)

def thankPage(request):
    if request.POST:
        name = request.POST['name'] 
        phone = request.POST['phone']
        element = Order(order_name = name, order_phone=phone)
        element.save()
        sendTelegram(tg_name=name,tg_phone=phone)
        return render(request, "./thanks.html", {'name': name, 'phone': phone})
    else:
        return render(request, "./thanks.html")