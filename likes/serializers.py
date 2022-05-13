from django.db import IntegrityError
from rest_framework import serializers
from likes.models import Like


class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer for handling of duplicate likes.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """
        Fields displayed on the Admin panel.
        """
        model = Like
        fields = ['id', 'created_at', 'owner', 'post']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
