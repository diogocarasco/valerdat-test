from rest_framework import serializers
from .models import Prod
class ProdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prod
        fields = ["ref", "zipcode", "store", "amount"]