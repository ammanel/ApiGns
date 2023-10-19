from django.db import models
from compte.models import UtilisateurPersonalisee

#classe categorie équipement
class CategorieEquipement(models.Model):
    id = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=225)

    def __str__(self):
        return self.libelle
#classe categorie article
class CategorieArticle(models.Model):
    id = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=225)
    categorie_equipement = models.ForeignKey(CategorieEquipement, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.libelle

#classe série
class Serie(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=225)
    def __str__(self):
        return self.nom
#classe marque
class Marque(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=225)
    def __str__(self):
        return self.nom

#classe model
class Model(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=225)
    marque = models.ForeignKey(Marque, on_delete=models.SET_NULL, null=True)
    serie = models.ForeignKey(Serie, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.nom
#classe stock
class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    statut = models.CharField(max_length=225)
    quantite_article=models.PositiveIntegerField()
    def __str__(self):
        return self.quantite_article
#classe article
class Article(models.Model):
    id = models.AutoField(primary_key=True)
    categorie_article = models.ForeignKey(CategorieArticle, on_delete=models.SET_NULL, null=True)
    model = models.ForeignKey(Model, on_delete=models.SET_NULL, null=True)
    admin = models.ForeignKey(UtilisateurPersonalisee, on_delete=models.SET_NULL, null=True)
    stock = models.ForeignKey(Stock, on_delete=models.SET_NULL, null=True)
    nom=models.CharField(max_length=225,unique=True)
    prix=models.DecimalField(max_digits=10, decimal_places=2)
    description=models.CharField(max_length=225)
    quantite_article=models.PositiveIntegerField()
    type_aticle=models.CharField(max_length=225)

    def __str__(self):
        return self.nom

#classe switch
class Switch(Article):
    couche=models.CharField(max_length=225)
    nombre_port=models.PositiveIntegerField()
    
#classe routeur
class Routeur(Article):
    fonctionnalite=models.CharField(max_length=225)
    memoire=models.CharField(max_length=225)
    vitesse_du_circuit=models.IntegerField()
#classe serveur
class Server(Article):
    fonctionnalite=models.CharField(max_length=225)
    memoire=models.CharField(max_length=225)
    vitesse_du_circuit=models.IntegerField()
