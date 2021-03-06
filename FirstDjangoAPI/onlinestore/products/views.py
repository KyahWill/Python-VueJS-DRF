from django.http import JsonResponse
from .models import Product , Manufacturer


def product_list(request):
    products = Product.objects.all()
    data = {"products": list(products.values())}#.values("pk","name","manufacturer","description")
    response = JsonResponse(data)
    return response

def product_detail(request,pk):
    
    try:
        product = Product.objects.get(pk=pk)
        data = {"product":
            {
                "name":product.name,
                "manufacturer":product.manufacturer.name,
                "description":product.description,
                "photo":product.photo.url,
                "price":product.price,
                "shipping_cost":product.shipping_cost,
                "quantity":product.quantity,

            }
        }
        response = JsonResponse(data)
    except Product.DoesNotExist:
        response = JsonResponse(
            {
            "error":{
                "code": 404,
                "message":"product not found"
                }
            }, status = 404)

    return response

def manufacturer_list(request):
    manufacturer = Manufacturer.objects.all().filter(active = True)
    data = {"manufacturer": list(manufacturer.values())}#.values("pk","name","manufacturer","description")
    response = JsonResponse(data)
    return response

def manufacturer_detail(request,pk):
    
    try:
        manufacturer = Manufacturer.objects.get(pk=pk)
        product = Product.objects.all().filter(manufacturer = manufacturer)
        data = {"Manufacturer": {
            "name": manufacturer.name,
            "location":manufacturer.location,
            "active":manufacturer.active,
            },
            "products": list(product.values())#.filter(manufacturer = manufacturer,)),
        }
        response = JsonResponse(data)
    except Manufacturer.DoesNotExist:
        response = JsonResponse(
            {
            "error":{
                "code": 404,
                "message":"Manufacturer not found"
                }
            }, status = 404)

    return response


# from django.views.generic.detail import DetailView
# from django.views.generic.list import ListView class ProductDetailView(DetailView):
#     model = Product
#     template_name = "products/product_detail.html"


# class ProductListView(List View):
#     model = Product
#     Template_name = template_name = "products/product_list.html"