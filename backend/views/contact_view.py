from django import views
from django.shortcuts import render

__all__ = ('ContactView',)


class ContactView(views.View):
    def get(self, request):
        return render(request, 'backend/contact.html')
