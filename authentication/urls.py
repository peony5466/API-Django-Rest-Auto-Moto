from django.urls import path
from rest_framework_simplejwt.views import(
  TokenObtainPairView, 
  TokenRefreshView)
from authentication.views import UserCreationView, UserDetailView


urlpatterns = [
# Endpoint pour l'obtention du token (connexion)
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
# Endpoint pour le rafraîchissement du token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
# Route pour la LISTE (GET admin) et la CRÉATION (POST inscription) d'utilisateurs
    path('users/', UserCreationView.as_view(), name='user_list_create'),
# Route pour le DETAIL d'un utilisateur par ID
    path('users/<int:pk>', UserDetailView.as_view(), name = 'user_detail')
]
