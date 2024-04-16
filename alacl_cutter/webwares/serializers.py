from rest_framework import serializers
from .models import Set, Product, Technology,Category


class SetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Set
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"

class TechnologySerializer(serializers.ModelSerializer):

    class Meta:
        model = Technology
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"