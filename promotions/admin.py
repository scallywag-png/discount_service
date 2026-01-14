from django.contrib import admin
from .models import PromoCode



@admin.register(PromoCode)
class PromoCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount_type', 'value', 'is_active', 'used_count', 'usage_limit')
    search_fields = ('code',)
