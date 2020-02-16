from django.urls import path

from absence.api.views import get_all_promotions

app_name = 'absence'

urlpatterns = [
    path('promotions', get_all_promotions, name="allPromotionsApi"),
]