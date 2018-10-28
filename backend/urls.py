from django.urls import path
from backend import views

urlpatterns = [
    path('',                                    views.IndexView.as_view(),              name='index'),
    path('shop',                                views.ShopView.as_view(),               name='shop'),
    path('shop/<int:id_category>',              views.ShopView.as_view(),               name='shop-product'),
    path('product_details/<int:id_product>',    views.ProductDetailView.as_view(),      name='product-details'),
    path('contact',                             views.ContactView.as_view(),            name='contact'),
    path('about',                               views.AboutView.as_view(),              name='about'),
]
