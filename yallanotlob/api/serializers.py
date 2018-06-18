from rest_framework import serializers
from orders.models import Meal, Order

class MealSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Meal
        fields = ('id', 'name', 'description')


class OrderSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Order
        fields = ('id', 'notes', 'meals', 'date')
        read_only_fields = ['date']