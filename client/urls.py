from django.urls import path
from client import views

urlpatterns = [
    path('message',         views.ClientMessageView.as_view(),              name='message'),
]
