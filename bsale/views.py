from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Product

# Create your views here.

class CategoryView(viewsets.ModelViewSet):
	serializer_class = CategorySerializer
	queryset = Category.objects.all()

class ProductView(viewsets.ModelViewSet):
	serializer_class = ProductSerializer
	queryset = Product.objects.all()