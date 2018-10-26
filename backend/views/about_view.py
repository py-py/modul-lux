from django import views
from django.shortcuts import render

__all__ = ('AboutView',)


class AboutView(views.View):
    def get(self, request):
        return render(request, 'backend/about.html')
