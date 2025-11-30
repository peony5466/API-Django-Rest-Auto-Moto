from django.contrib.auth.models import User 
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model= User
    fields= ["id", "username", "password","email"]
    extra_kwargs={
      #s'assurer que le password n'est jamais retourné dans les reponses get
      'password': {'write_only' : True}
    }

# Surcharge la méthode create() pour hacher le mot de passe avant de sauvegarder l'utilisateur.
  def create(self, validated_data):
    #methode create_user de django gere le hachage du password
    user= User.objects.create_user(**validated_data)
    return user