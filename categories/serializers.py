from rest_framework import serializers
from categories.models import Category


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for Category model.
    """
    category = serializers.ReadOnlyField(source='category.category')

    class Meta:
        """
        Fields displayed on the Admin panel.
        """
        model = Category
        fields = ['id', 'created_at', 'updated_at', 'category']
