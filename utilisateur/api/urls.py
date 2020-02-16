from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from utilisateur.api.views import user_connecte

app_name = 'utilisateur'

urlpatterns = [
    path('connexion', obtain_auth_token, name="connexionApi"),
    path('user_connecte', user_connecte, name="userConnecteApi"),
]