from rest_framework import serializers

class ApplyPromoSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=20)
    cart_total = serializers.DecimalField(max_digits=10, decimal_places=2)