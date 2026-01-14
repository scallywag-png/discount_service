from django.db import models


class PromoCode(models.Model):
    DISCOUNT_TYPES = [
        ('PERCENT', 'Відсоток (%)'),
        ('FIXED', 'Фіксована сума (UAH)'),
    ]


    code = models.CharField(max_length=20, unique=True)
    discount_type = models.CharField(max_length=10, choices=DISCOUNT_TYPES, default='PERCENT')
    value = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    usage_limit = models.PositiveIntegerField(default=100)
    used_count = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"{self.code} ({self.value} {self.discount_type})"
