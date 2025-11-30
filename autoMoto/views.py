from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
from autoMoto.models import Concessionnaire, Vehicule
from rest_framework.permissions import IsAuthenticated
from autoMoto.serializers import ConcessionnaireListSerializer, ConcessionnaireDetailSerializer, VehiculeSerializer

# Create your views here.
#"ListCreateAPIView" gère la liste get et la creation post 
class ConcessionnaireListView(APIView):
  #Seuls les utilisateurs authentifiés peuvent accéder à la vue
  permission_classes = [IsAuthenticated]
  def get(self, request):
    concessionnaires = Concessionnaire.objects.all()
    serializer = ConcessionnaireListSerializer(concessionnaires, many=True)
    return Response(serializer.data)
  
  def post(self, request):
    # Utilise le serializer Detail (qui nécessite le SIRET) pour la création.
    serializer = ConcessionnaireDetailSerializer(data= request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=HTTP_201_CREATED)
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
  
# Gère le DÉTAIL (GET), la MODIFICATION (PUT) et la SUPPRESSION (DELETE) d'un concessionnaire par son ID (pk).
class ConcessionnaireDetailView(APIView):
  permission_classes = [IsAuthenticated]

  def get_object(self,pk):
    #récupérer un concessionnaire, renvoie 404 si non trouvé.
    return get_object_or_404(Concessionnaire, pk= pk)

  def get(self,request, pk):
    concessionnaire = self.get_object(pk)
    serializer = ConcessionnaireDetailSerializer(concessionnaire)
    return Response(serializer.data)
  
  def put(self, request, pk):
    concessionnaire=self.get_object(pk)
    serializer = ConcessionnaireDetailSerializer(concessionnaire, data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors , status= HTTP_400_BAD_REQUEST)
  
  def delete(self, request, pk):
    # Supprime le concessionnaire (et tous les véhicules associés grâce à CASCADE).
    concessionnaire= self.get_object(pk)
    concessionnaire.delete()
    return Response(status=HTTP_204_NO_CONTENT)
  
# Gère la LISTE (GET) des véhicules pour un concessionnaire spécifique (via concessionnaire_pk) 
# et la CRÉATION (POST) d'un nouveau véhicule pour ce concessionnaire.
class VehiculeListCreateView(APIView):
  permission_classes=[IsAuthenticated]
  def get(self, request, concessionnaire_pk):
    # Filtre les véhicules appartenant à l'ID de concessionnaire donné dans l'URL.
    concessionnaire = get_object_or_404(Concessionnaire, pk= concessionnaire_pk)
    vehicules= concessionnaire.vehicules.all()
    serializer = VehiculeSerializer(vehicules, many =True)
    return Response(serializer.data)
  
  def post(self,request, concessionnaire_pk):
    # Récupère le concessionnaire et lie le véhicule à lui lors de la sauvegarde.
    concessionnaire=get_object_or_404(Concessionnaire, pk= concessionnaire_pk)
    serializer= VehiculeSerializer(data = request.data)
    if serializer.is_valid():
      # Attribue le concessionnaire au véhicule avant de sauvegarder.
      serializer.save(concessionnaire = concessionnaire)
      return Response(serializer.data, status=HTTP_201_CREATED)
    return Response(serializer.errors, status= HTTP_400_BAD_REQUEST)
  
# Gère le DÉTAIL (GET), la MODIFICATION (PUT/PATCH) et la SUPPRESSION (DELETE) d'un véhicule spécifique, 
# en vérifiant qu'il est bien lié au concessionnaire parent (concessionnaire_pk).
class vehiculeDetailView(APIView):
  permission_classes = [IsAuthenticated]
  def get_object(self, concessionnaire_pk,pk):
    # Récupère le véhicule par son ID (pk) et s'assure qu'il appartient au concessionnaire parent.
    concessionnaire = get_object_or_404(Concessionnaire, pk= concessionnaire_pk)
    return get_object_or_404(Vehicule, pk=pk, concessionnaire=concessionnaire)
  
  def get(self, request, concessionnaire_pk,pk):
    vehicule= self.get_object(concessionnaire_pk,pk)
    serializer = VehiculeSerializer(vehicule)
    return Response(serializer.data)
  
  def put(self, request , concessionnaire_pk, pk):
    vehicule= self.get_object(concessionnaire_pk,pk)
    serializer = VehiculeSerializer(vehicule, data= request.data, partial= True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
  
  def delete(self, request, concessionnaire_pk, pk):
    vehicule = self.get_object(concessionnaire_pk,pk)
    vehicule.delete()
    return Response(status=HTTP_204_NO_CONTENT)
  