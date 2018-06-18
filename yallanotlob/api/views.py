from rest_framework import generics #, permissions
from .serializers import MealSerializer, OrderSerializer
from orders.models import Meal, Order

# Create your views here.


class MealMixin(object):
    model = Meal
    queryset = Meal.objects.all()
    serializer_class = MealSerializer


class MealList(MealMixin, generics.ListCreateAPIView):
    pass


class MealDetail(MealMixin, generics.RetrieveUpdateDestroyAPIView):
    pass


class OrderMixin(object):
    model = Order
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderList(OrderMixin, generics.ListCreateAPIView):
    pass


class OrderDetail(OrderMixin, generics.RetrieveUpdateDestroyAPIView):
    pass


class OrderMealList(OrderMixin, generics.ListAPIView):
    def get_queryset(self):
        queryset = super(OrderMealList, self).get_queryset()
        return queryset.filter(meals__pk=self.kwargs.get('pk'))