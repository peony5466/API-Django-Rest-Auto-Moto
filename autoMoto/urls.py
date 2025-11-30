from django.urls import path

from autoMoto.views import ConcessionnaireListView, ConcessionnaireDetailView, VehiculeListCreateView, vehiculeDetailView
urlpatterns = [
  #route pour get et post de concessionnaires
    path('concessionnaires/', ConcessionnaireListView.as_view()),
  #route pour detail get , modification put/patch, suppression delete dun concessionnaire 
    path('concessionnaires/<int:pk>', ConcessionnaireDetailView.as_view(), name='concessionnaire-detail'),
  # route pour get et post de vehicules
    path('concessionnaires/<int:concessionnaire_pk>/vehicules/', VehiculeListCreateView.as_view(), name='Vehicule-list-create'),
  #route detail, modification, suppression d'un vehicule
    path('concessionnaires/<int:concessionnaire_pk>/vehicules/<int:pk>', vehiculeDetailView.as_view(), name='Vehicule-detail'),
]