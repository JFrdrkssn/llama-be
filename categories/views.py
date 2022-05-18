from rest_framework import generics, permissions
from categories.models import Category
from categories.serializers import CategorySerializer


class CategoryList(generics.ListCreateAPIView):
    """
    List categories.
    """
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()


class CategoryDetail(generics.RetrieveAPIView):
    """
    Retrieve a category to view posts of specific category.
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
