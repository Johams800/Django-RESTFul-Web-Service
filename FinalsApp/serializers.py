from rest_framework import serializers

from .models import Customer, Address, Order, OrderItems


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'customer_since', 'prime_customer']
        read_only_fields = ['prime_customer']


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'street', 'city', 'state', 'zipCode', 'customer']

    def validate(self, data):
        if len(data['zipCode']) < 5 or len(data['zipCode']) > 5:
            raise serializers.ValidationError("Invalid Zip Code")
        return data


class AddressSerializerForUpdate(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'street', 'city', 'state', 'zipCode', 'customer']
        read_only_fields = ['customer']

    def validate(self, data):
        if len(data['zipCode']) < 5 or len(data['zipCode']) > 5:
            raise serializers.ValidationError("Invalid Zip Code")
        return data


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'order_number', 'order_date', 'order_total', 'payment_type', 'account_number',
                  'expiration_date', 'customer']
        read_only_fields = ['order_total', 'expiration_date']


class OrderSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'order_number', 'order_date', 'order_total', 'payment_type', 'account_number',
                  'expiration_date', 'customer']
        read_only_fields = ['order_total', 'expiration_date', 'customer']


class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = ['id', 'item_description', 'item_quantity', 'cost', 'order']
        read_only_fields = ['cost']

    def validate(self, data):
        order = data['order']
        order_num = Order.objects.get(order_number=order)
        qty = data['item_quantity']
        price = 50
        prime_customer = 250
        if data['item_quantity']:
            data['cost'] = qty * price
            order_num.order_total = order_num.order_total + data['cost']
            order_num.save()
        if order_num.order_total > prime_customer:
            customer = Customer.objects.get(id=order_num.customer.id)
            customer.prime_customer = 'P'
            customer.save(update_fields=['prime_customer'])
        return data

