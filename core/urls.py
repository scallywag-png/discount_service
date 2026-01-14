from django.contrib import admin
from django.urls import path
from promotions.views import apply_promo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/apply-promo/', apply_promo),
]