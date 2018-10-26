from django import views
from django.shortcuts import render

__all__ = ('ShopView',)


class ShopView(views.View):
    def get(self, request):
        return render(request, 'backend/shop.html')
