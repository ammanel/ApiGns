from django.db import models
from compte.models import UtilisateurPersonalisee
class InfoSecurite(models.Model):
    id = models.AutoField(primary_key=True)
    utilisateur = models.ForeignKey(UtilisateurPersonalisee, on_delete=models.SET_NULL, null=True)
    date_heure = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=225)
    type_objet = models.CharField(max_length=225)
    object_id = models.PositiveIntegerField()

    def __str__(self):
        return f'user: {self.utilisateur}, action: {self.action}, objet: {self.type_objet} '