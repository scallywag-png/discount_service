from django.db import transaction
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import PromoCode
from .serializers import ApplyPromoSerializer
from .services import DiscountCalculator


@api_view(['POST'])
def apply_promo(request):

    serializer = ApplyPromoSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    code = serializer.validated_data['code']
    cart_total = serializer.validated_data['cart_total']

    try:
        with transaction.atomic():
            promo = PromoCode.objects.select_for_update().get(code=code)

            if not promo.is_active:
                return Response({"error": "Цей промокод вимкнено"}, status=400)

            if promo.used_count >= promo.usage_limit:
                return Response({"error": "Ліміт використання вичерпано"}, status=400)

            final_price, discount = DiscountCalculator.calculate_final_price(cart_total, promo)
            promo.used_count += 1
            promo.save()

            return Response({
                "valid": True,
                "original_price": cart_total,
                "discount_amount": discount,
                "new_price": final_price,
                "message": "Промокод успішно застосовано!"
            })


    except PromoCode.DoesNotExist:
        return Response({"error": "Промокод не знайдено"}, status=404)
    except Exception as e:
        return Response({"error": str(e)}, status=500)