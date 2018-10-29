from django import views
from django.http import JsonResponse, Http404
from django.shortcuts import render
from django.urls import reverse

from backend.models import Product

__all__ = ('ProductDetailView', 'ProductDetailAjaxView',)


class ProductDetailView(views.View):
    def get(self, request, id_product):
        try:
            product = Product.active_objects.get(id=id_product)
        except Product.DoesNotExist as e:
            raise Http404
        else:
            context = {
                'product': product,
            }
        return render(request, 'backend/product-details.html', context=context)


class ProductDetailAjaxView(views.View):
    def get(self, request):
        id_product = request.GET['id_product']

        try:
            product = Product.active_objects.get(id=int(id_product))
        except (Product.DoesNotExist, ValueError):
            data = {}
            status = 400
        else:
            data = {
                'id': product.id,
                'name': product.name,
                'self_url': reverse('backend:product-details', kwargs={'id_product': product.id}),
                'description': product.description,
                'images': [image.image.url for image in product.images.all()],
            }
            status = 200

        return JsonResponse(data=data, status=status)
