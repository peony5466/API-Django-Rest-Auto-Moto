from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth.models import User
from authentication.serializers import UserSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.views import APIView
# Create your views here.
# Gère la LISTE (GET /api/users/) et la CRÉATION (POST /api/users/)
class UserCreationView(ListCreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

# Redéfinit les permissions pour différencier GET et POST
  def get_permissions(self):
    # Si c'est une requête POST (inscription), aucune permission n'est requise
    if self.request.method == 'POST':
      return []
    #seul l'admin peut voir liste users
    return [IsAdminUser()]
    
class UserDetailView(RetrieveUpdateDestroyAPIView):
  queryset= User.objects.all()
  serializer_class = UserSerializer

  permission_classes= [IsAdminUser]