from django.db import models
from compte.models import UtilisateurPersonalisee
from produit.models import Article


#classe mode de paiement
class ModePaiement(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=225)
    def __str__(self):
        return self.nom
    

#classe societe d'expedition
class SocieteExpedition(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=225)
    def __str__(self):
        return self.nom

#classe ligne commande
class LigneCommande(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UtilisateurPersonalisee, on_delete=models.SET_NULL, null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now=True)
    quantite = models.PositiveIntegerField(default=1)
    statut= models.BooleanField(default=False)


#classe panier
class Panier(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(UtilisateurPersonalisee, on_delete=models.CASCADE, null=True)
    lignes_commande= models.ManyToManyField(LigneCommande)

    def __str__(self):
        return self.user.nom

#classe commande
class Commande(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UtilisateurPersonalisee, on_delete=models.SET_NULL, null=True)
    societe_expedition = models.ForeignKey(SocieteExpedition, on_delete=models.SET_NULL, null=True)
    mode_paiement = models.ForeignKey(ModePaiement, on_delete=models.SET_NULL, null=True)
    num_commande = models.PositiveIntegerField()
    date=models.DateTimeField(auto_now=True)
    lignes_commande= models.ManyToManyField(LigneCommande)
    nom_destinataire= models.CharField(max_length=225)
    addresse = models.CharField(max_length=225)
    ville = models.CharField(max_length=225)
    pays = models.CharField(max_length=225)
    contact = models.CharField(max_length=225)
    statut= models.BooleanField(default=False)

    def __str__(self):
        return self.user.nom


#classe facture
class Facture(models.Model):
    id = models.AutoField(primary_key=True)
    commande= models.ForeignKey(Commande, on_delete=models.SET_NULL, null=True)
    num_facture = models.PositiveIntegerField()
    date=models.DateTimeField(auto_now=True)
    total= models.PositiveIntegerField()

    def __str__(self):
        return self.num_facture


#classe transaction
class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    commande= models.ForeignKey(Commande, on_delete=models.SET_NULL, null=True)
    num_transaction =  models.CharField(max_length=225)
    montant = models.PositiveIntegerField()

    def __str__(self):
        return self.num_transaction
    
