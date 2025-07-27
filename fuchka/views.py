from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Fuchka
from datetime import timedelta
from .models import CartItem
from django.http import JsonResponse
from django.shortcuts import redirect
from urllib.parse import quote
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
def home(request):
    query = request.GET.get('query')
    if query:
        fuchka = Fuchka.objects.filter(name__icontains=query)
    else:
        fuchka = Fuchka.objects.all()
    return render(request, 'home.html', {'fuchka': fuchka})

def product_page(request):
    # Delete cart items older than 12 hours
    cutoff = timezone.now() - timedelta(hours=12)
    CartItem.objects.filter(added_at__lt=cutoff).delete()

    # Load current cart
    cart_items = CartItem.objects.all()
    return render(request, 'products.html', {'cart_items': cart_items})


def add_to_cart(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        CartItem.objects.create(name=name, price=price)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'}, status=400)
def order_whatsapp(request):
    # Clean expired cart items
    CartItem.objects.filter(added_at__lt=timezone.now() - timedelta(hours=12)).delete()

    # Get current items
    items = CartItem.objects.all().values('name', 'price')
    if not items:
        return redirect('/')  # no items, go home

    # Build message text
    message = "Hi, I want to order:\nItem Name — Price — Quantity\n"
    seen = set()
    for item in items:
        key = f"{item['name']} — Taka {item['price']} — "
        if key not in seen:
            seen.add(key)
            message += f"- {key}\n"

    # Encode and redirect to WhatsApp
    whatsapp_url = "https://wa.me/8801729985668?text=" + quote(message)
    return redirect(whatsapp_url)
@csrf_exempt
def remove_cart_item(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(CartItem, id=item_id)
        item.delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'}, status=400)