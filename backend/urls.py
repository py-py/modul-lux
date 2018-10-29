from django.urls import path
from backend import views

urlpatterns = [
    path('',                                    views.IndexView.as_view(),              name='index'),
    path('shop',                                views.ShopView.as_view(),               name='shop'),
    path('shop/<int:id_category>',              views.ShopView.as_view(),               name='shop-products'),
    path('products/<int:id_product>',           views.ProductDetailView.as_view(),      name='product-details'),
    path('contact',                             views.ContactView.as_view(),            name='contact'),
    path('about',                               views.AboutView.as_view(),              name='about'),

    path('ajax/products',                       views.ProductDetailAjaxView.as_view(),  name='ajax-product-details'),
]
