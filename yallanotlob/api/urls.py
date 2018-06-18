from django.conf.urls import url, include
#from rest_framework.urlpatterns import format_suffix_patterns

from . import views

meal_urls = [
    url(r'^$', views.MealList.as_view(), name='meal-list'),
    url(r'^(?P<pk>[0-9]+)$', views.MealDetail.as_view(), name='meal-detail'),
]

order_urls = [
    url(r'^$', views.OrderList.as_view(), name='order-list'),
    url(r'^(?P<pk>[0-9]+)$', views.OrderDetail.as_view(), name='order-detail'),
    url(r'^(?P<pk>[0-9]+)/meals$', views.OrderDetail.as_view(), name='ordermeal-list'),
]

urlpatterns = [
    url(r'^meals', include(meal_urls)),
    url(r'^orders', include(order_urls)),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
