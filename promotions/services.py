from decimal import Decimal


class DiscountCalculator:
    @staticmethod
    def calculate_final_price(cart_total, promo_code):
        cart_total = Decimal(str(cart_total))
        discount_amount = Decimal(0)

        if promo_code.discount_type == 'PERCENT':
            discount_amount = cart_total * (promo_code.value / 100)
        elif promo_code.discount_type == 'FIXED':
            discount_amount = promo_code.value
        if discount_amount > cart_total:
            discount_amount = cart_total

        final_price = cart_total - discount_amount

        return final_price, discount_amount