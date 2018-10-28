from django import views
from django.shortcuts import render

from backend.models import Category, Product

__all__ = ('ShopView',)


class ShopView(views.View):
    def get(self, request, id_category=None):
        categories = Category.active_objects.all()
        context = {
            'categories': categories,
        }

        if id_category:
            try:
                category = Category.active_objects.get(id=id_category)
            except Category.DoesNotExist:
                pass
            else:
                products = Product.active_objects.filter(category=category)
                context['products'] = products

        return render(request, 'backend/shop.html', context=context)
