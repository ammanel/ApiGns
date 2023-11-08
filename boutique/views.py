from django.shortcuts import render
from django.contrib.sessions.models import Session
from produit.models import Article
from boutique.models import *
from boutique.serializers import *  
from rest_framework.response import Response  
from rest_framework.views import APIView  
from rest_framework import status  
import random
from securite.models import InfoSecurite  

#fonction pour ajouter un article au panier quand l'utilisateur est connecté uniquement
class AjouterAuPanierAPIView(APIView):
    def post(self, request,id_produit):
        user = request.user
        article = Article.objects.get(id=id_produit)

        panier, _ = Panier.objects.get_or_create(user=user)
        commande,creer=LigneCommande.objects.get_or_create(user=user,article=article) 
        if creer:
            panier.lignes_commande.add(commande)
            panier.save()

        else:
            commande.quantite +=1
            commande.save()
        return Response({"message": "produit ajouter au panier avec succès"}, status=status.HTTP_201_CREATED)

#fonction pour supprimer un article du panier
class SupprimerDuPanierAPIView(APIView):
    def delete(self, request, id_produit):
        user = request.user
        produit = Article.objects.get(id=id_produit)

        try:
            panier = Panier.objects.get(user=user)
            commande = LigneCommande.objects.get(user=user, article=produit)
            panier.lignes_commande.remove(commande)
            commande.delete()

            return Response({"message": "L'article a été supprimé du panier avec succès."}, status=status.HTTP_200_OK)

        except (Article.DoesNotExist, Panier.DoesNotExist, LigneCommande.DoesNotExist):
            return Response({"error": "L'article ou le panier n'existe pas."}, status=status.HTTP_404_NOT_FOUND)


#fonction pour valider un panier et lancer une commande 
class ValiderUnPanierAPIView(APIView):
    def post(self, request,id_panier):
        user = request.user
        panier = Panier.objects.get(id=id_panier)
        commandes_panier = PanierLigneCommande.objects.filter(panier=panier)
        serializer = CommandeSerializer(data=request.data)  

        if serializer.is_valid():  
            random_number = random.randint(1, 1000)
            commande_obj=serializer.save(user=user,num_commande=random_number) 
           
            for ligne_commande in commandes_panier:
                commande = LigneCommande.objects.get(id=ligne_commande.ligne_commande.id)
                commande.statut=True
                commande.save()
                commande_obj.lignes_commande.add(commande) 
                commande_obj.save()

            InfoSecurite.objects.create(utilisateur=user,action="créer",type_objet="commande",object_id=commande_obj.id) 
            return Response(serializer.data, status=status.HTTP_201_CREATED)    

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  



    
               