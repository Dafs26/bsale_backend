from django.shortcuts import render
from rest_framework import viewsets, filters, generics
from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Product

# Create your views here.

class CategoryView(viewsets.ModelViewSet):
	serializer_class = CategorySerializer
	queryset = Category.objects.all()
	filter_backends = [filters.SearchFilter]

	search_fields = [
		'name',
	]

class ProductView(viewsets.ModelViewSet):
	serializer_class = ProductSerializer
	queryset = Product.objects.all()
	filter_backends = [filters.SearchFilter]

	search_fields = [
		'name',
		'category__name',
	]
