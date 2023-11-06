from django.shortcuts import render
from django.contrib.sessions.models import Session
from produit.models import Article
from boutique.models import LigneCommande,Panier
from rest_framework.response import Response  
from rest_framework.views import APIView  
from rest_framework import status  

#fonction pour ajouter un article au panier quand l'utilisateur est connecté uniquement
class AjouterAuPanierAPIView(APIView):
    def post(self, request,id_produit):
        user = request.user
        produit = Article.objects.get(id=id_produit)

        panier, _ = Panier.objects.get_or_create(user=user)
        commande,creer=LigneCommande.objects.get_or_create(user=user,article=produit) 
        if creer:
            panier.lignes_commande.add(commande)
            panier.save()

        else:
            commande.quantite +=1
            commande.save()
        return Response({"message": "produit ajouter au panier avec succès"}, status=status.HTTP_201_CREATED)

    

# #fonction pour valider un panier et lancer une commande 
# class ValiderUnPanierAPIView(APIView):
#     def get(self, request,id_panier):
#         user = request.user
#         panier = Panier.objects.get(id=id_panier)
#         ligne_avec_panier = Panier_lignes_commande.objects.filter(
#                 panier_id=panier
#             )

#         return Response({"message": "panier"}, ligne_avec_panier,status=status.HTTP_201_CREATED)

    
               