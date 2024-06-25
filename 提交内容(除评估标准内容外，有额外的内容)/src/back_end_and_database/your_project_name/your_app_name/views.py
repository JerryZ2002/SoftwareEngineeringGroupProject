# Create your views here.
# from django.http import JsonResponse
from django.db.models import Q

from your_app_name.models import Product
from .models import Product_info, PurchaseOrder, SalesOrder, Inventory

from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework import status
from .serializers import ProductSerializer
from .serializers import ProductInfoSerializer, PurchaseOrderSerializer, SalesOrderSerializer, InventorySerializer
from rest_framework import viewsets

from django.shortcuts import render

from django.views import View
from django.http import JsonResponse
class ProductInfoAPI(View):
    def get(self,request,*args,**kwargs):
        data=Product_info.objects.value()
        return JsonResponse(list(data),safe=False)

def home(request):
    return render(request, 'home.html')

@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def add_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_product(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def update_product(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # update the product name and price
    product.name = request.data.get('name', product.name)
    product.price = request.data.get('price', product.price)
    product.save()

    return Response(status=status.HTTP_200_OK)



class ProductInfoViewSet(viewsets.ModelViewSet):
    queryset = Product_info.objects.all() #allow all calls, such as get, post, delete, etc., very convenient
    serializer_class = ProductInfoSerializer

    @action(detail=False, methods=['GET'])
    def search(self, request):
        # obtain the query parameter, such as product name
        query = request.GET.get('query', '')
        field = request.GET.get('field', 'product_id')
        # use icon contains for fuzzy query
        if field not in [field.name for field in Product_info._meta.get_fields()]:
            return Response({'error': 'Invalid field specified'}, status=400)

        filter_kwargs = {f'{field}__icontains': query}
        results = Product_info.objects.filter(**filter_kwargs)
        # return the query result serialized
        serializer = self.get_serializer(results, many=True)
        return Response(serializer.data)

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()  #allow all calls, such as get, post, delete, etc., very convenient
    serializer_class = PurchaseOrderSerializer

    @action(detail=False, methods=['GET'])
    def search(self, request):
        # obtain the query parameter, such as product name
        query = request.GET.get('query', '')
        field = request.GET.get('field', 'order_number')  # default search field is order number
        # use icontains for fuzzy query
        if field not in [field.name for field in PurchaseOrder._meta.get_fields()]:
            return Response({'error': 'Invalid field specified'}, status=400)

        filter_kwargs = {f'{field}__icontains': query}
        results = PurchaseOrder.objects.filter(**filter_kwargs)
        # return the query result serialized
        serializer = self.get_serializer(results, many=True)
        return Response(serializer.data)


class SalesOrderViewSet(viewsets.ModelViewSet):
    queryset = SalesOrder.objects.all()
    serializer_class = SalesOrderSerializer

    @action(detail=False, methods=['GET'])
    def search(self, request):
        # obtain the query parameter, such as product name
        query = request.GET.get('query', '')
        field = request.GET.get('field', 'order_number')
        # use icontains for fuzzy query
        if field not in [field.name for field in SalesOrder._meta.get_fields()]:
            return Response({'error': 'Invalid field specified'}, status=400)

        filter_kwargs = {f'{field}__icontains': query}
        results = SalesOrder.objects.filter(**filter_kwargs)
        # return the query result serialized
        serializer = self.get_serializer(results, many=True)
        # return 1
        return Response(serializer.data)


class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

    @action(detail=False, methods=['GET'])
    def search(self, request):
        # obtain the query parameter, such as product name
        query = request.GET.get('query', '')
        field = request.GET.get('field', 'product_id')
        # use icontains for fuzzy query
        if field not in [field.name for field in Inventory._meta.get_fields()]:
            return Response({'error': 'Invalid field specified'}, status=400)

        filter_kwargs = {f'{field}__icontains': query}
        results = Inventory.objects.filter(**filter_kwargs)
        # return the query result serialized
        serializer = self.get_serializer(results, many=True)
        return Response(serializer.data)
