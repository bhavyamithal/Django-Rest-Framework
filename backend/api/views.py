import json
from django.http import JsonResponse
from products.models import Product

def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    data['id'] = model_data.id
    data['title'] = model_data.title
    data['description'] = model_data.description
    data['price'] = model_data.price
    # data['summary'] = model_data.summary
    # data['featured'] = model_data.featured
    return JsonResponse(data)
