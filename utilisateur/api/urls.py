from django.urls import path

from utilisateur.api.views import user_with_token

app_name = 'utilisateur'

urlpatterns = [
    path('userAPI', user_with_token, name="listEtuApi"),
]