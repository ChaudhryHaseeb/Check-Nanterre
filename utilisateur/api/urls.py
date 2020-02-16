from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from utilisateur.api.views import user_connecte, user_modifier_mdp, user_reset_mdp

app_name = 'utilisateur'

urlpatterns = [
    path('connexion', obtain_auth_token, name="connexionApi"),
    path('user_connecte', user_connecte, name="userConnecteApi"),
    path('modifier_mdp', user_modifier_mdp, name="userModifierMdpApi"),
    path('reset_mdp', user_reset_mdp, name="userResetMdpApi"),
]