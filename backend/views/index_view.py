from django import views
from django.shortcuts import render

__all__ = ('IndexView',)


class IndexView(views.View):
    def get(self, request):
        return render(request, 'backend/index.html')
