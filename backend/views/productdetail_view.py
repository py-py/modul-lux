from django import views
from django.shortcuts import render

__all__ = ('ProductDetailView',)


class ProductDetailView(views.View):
    def get(self, request, id_product):
        context = {
            'id_product': id_product,
        }
        return render(request, 'backend/product-details.html', context=context)
