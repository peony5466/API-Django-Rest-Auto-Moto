from django.db.models import Model, CharField,IntegerField, FloatField, DateTimeField, ForeignKey, CASCADE
from django.core.validators import RegexValidator
# Create your models here.
class Concessionnaire(Model):
  #nom du concessionnaire limité a 64 caractere
  nom = CharField(max_length=64)
  #siret limité a 14 chiffres + validation
  siret = CharField(max_length=14, validators=[RegexValidator(r'^\d{14}$', message='Le SIRET doit contenir 14 chiffres')])
  #ce n’est pas demandé, mais j’ai pris l’habitude de le faire
  created_at = DateTimeField(auto_now_add=True)
  updated_at = DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.nom


class Vehicule(Model):
  #choix pour le champ type du modele Vehicule
  TYPE_CHOICES = [('moto','Moto'), ('auto','Auto')]
  #clé etrangere vers Concessionnaire 
  concessionnaire=ForeignKey(Concessionnaire, related_name='vehicules', on_delete=CASCADE)
  #type de Vhicule (soit 'auto' ou 'moto')
  type= CharField(max_length=4, choices=TYPE_CHOICES)
  marque = CharField(max_length=64)
  cheveaux = IntegerField()
  prix_ht = FloatField()
  created_at = DateTimeField(auto_now_add=True)
  updated_at = DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.marque}({self.type})"