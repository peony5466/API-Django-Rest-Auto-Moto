from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import Concessionnaire, Vehicule
#serializer Concessionnaire : Liste(Get/api/concessionnaires)
class ConcessionnaireListSerializer(ModelSerializer):
  class Meta:
    model = Concessionnaire
    #champs minimalistes pour une liste
    fields= ['id', 'nom']

#details: creation et modifications dun concessionnaire(get, post, put , delete /api/concessionnaires/<id>/)
class ConcessionnaireDetailSerializer(ModelSerializer):
  class Meta:
    model= Concessionnaire
    #liste des champs sans le 'siret'
    fields= ['id', 'nom']

#serializer Vehicule
class VehiculeSerializer(ModelSerializer):
  #clé etragere en lecture seule : on renvoie son ID mais on ne l'envoie pas dans le JSON,
  # car il est récupéré depuis l'URL.
  concessionnaire = PrimaryKeyRelatedField(read_only = True)

  class Meta:
    model = Vehicule
    #inclut ts les champs du modele (type, marque, chevaux, prix_ht,etc)
    fields = '__all__'