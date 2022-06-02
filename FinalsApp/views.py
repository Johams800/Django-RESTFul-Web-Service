from rest_framework import viewsets
from rest_framework.response import Response

from .models import Customer, Address, Order, OrderItems
from .serializers import CustomerSerializer, AddressSerializer, AddressSerializerForUpdate, \
    OrderSerializer, OrderSerializerUpdate, OrderItemsSerializer


# Create your views here.

# Create a customer
class AddCustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    http_method_names = ['get', 'post', 'head', 'options']

    def create(self, request, *args, **kwargs):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            customer = serializer.save()
            return Response(CustomerSerializer(customer).data)
        else:
            return Response({"message": "Could not create the Customer"})


# Returns all the customers it has in the database
class GetCustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    http_method_names = ['get']

    def list(self, request):
        queryset = Customer.objects.all()
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)


# Updates an existing customer
class UpdateCustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    http_method_names = ['get', 'put']

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, pk, *args, **kwargs):
        customer = Customer.objects.get(id=pk)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response({"message": "Could not update the Customer"})
        return Response(CustomerSerializer(customer).data)


# Creates a new Address and links it with an existing Customer
class AddAddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    http_method_names = ['get', 'post', 'head', 'options']

    def retrieve(self, request, pk, *args, **kwargs):
        address = Address.objects.get(id=pk)
        serializer = AddressSerializer(address)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            address = serializer.save()
            return Response(AddressSerializer(address).data)
        else:
            return Response({"message": "Could not create the Address"})


# Returns all the Addresses associated with a customer
class GetAddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    http_method_names = ['get']

    def retrieve(self, request, pk, *args, **kwargs):
        address = Address.objects.filter(customer=pk)
        if not address:
            return Response({'error': "No query found!"})
        else:
            serializer = AddressSerializer(address, many=True)
            return Response(serializer.data)


# Updates an Address
class UpdateAddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializerForUpdate
    http_method_names = ['get', 'put']

    def retrieve(self, request, pk, *args, **kwargs):
        address = Address.objects.get(id=pk)
        serializer = AddressSerializerForUpdate(address)
        return Response(serializer.data)

    def update(self, request, pk, *args, **kwargs):
        address = Address.objects.get(id=pk)

        serializer = AddressSerializerForUpdate(address, data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response({"message": "Could not update the Customer"})
        return Response(AddressSerializerForUpdate(address).data)


class AddOrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ['get', 'post', 'head', 'options']

    def create(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.save()
            return Response(OrderSerializer(order).data)
        else:
            return Response({"message": "Could not create the Customer"})

    def list(self, request):
        queryset = Order.objects.all()
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)


class UpdateOrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializerUpdate
    http_method_names = ['get', 'put']

    def retrieve(self, request, pk, *args, **kwargs):
        order = Order.objects.get(id=pk)
        serializer = OrderSerializerUpdate(order)
        return Response(serializer.data)

    def update(self, request, pk, *args, **kwargs):
        order = Order.objects.get(id=pk)

        serializer = OrderSerializerUpdate(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response({"message": "Could not update the Order"})
        return Response(OrderSerializerUpdate(order).data)


class GetOrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ['get']

    def retrieve(self, request, pk, *args, **kwargs):
        order = Order.objects.filter(customer=pk)
        if not order:
            return Response({'error': "No query found!"})
        else:
            serializer = OrderSerializer(order, many=True)
            return Response(serializer.data)


class AddProductViewSet(viewsets.ModelViewSet):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializer
    http_method_names = ['get', 'post', 'head', 'options']

    def create(self, request, *args, **kwargs):
        serializer = OrderItemsSerializer(data=request.data)
        if serializer.is_valid():
            order_item = serializer.save()
            return Response(OrderItemsSerializer(order_item).data)
        else:
            return Response({"message": "Could not create the Address"})


class GetProductsViewSet(viewsets.ModelViewSet):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializer
    http_method_names = ['get']

    def retrieve(self, request, pk, *args, **kwargs):
        order_item = OrderItems.objects.filter(order=pk)
        if not order_item:
            return Response({'error': "No query found!"})
        else:
            serializer = OrderItemsSerializer(order_item, many=True)
            return Response(serializer.data)

