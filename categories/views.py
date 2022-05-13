from rest_framework import generics
from categories.models import Category
from categories.serializers import CategorySerializer


class CategoryList(generics.ListAPIView):
    """
    List categories.
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryDetail(generics.RetrieveAPIView):
    """
    Retrieve a category to view posts of specific category.
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
