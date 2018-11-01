from django import views
from django.shortcuts import render

from backend.models import Product

__all__ = ('IndexView',)


class IndexView(views.View):
    def get(self, request):
        featured_products = Product.active_objects.order_by('-date_updated')[:10]
        context = {
            'featured_products': featured_products,
        }
        return render(request, 'backend/index.html', context=context)
