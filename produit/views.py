from django.shortcuts import render
from rest_framework.views import APIView  
from rest_framework import status  
from rest_framework.response import Response  
from produit.models import *  
from securite.models import InfoSecurite  
from produit.serializers import *  
from rest_framework.permissions import IsAuthenticated,IsAdminUser

#Classe pour lister toutes les categorie d'équipement 
class CategorieEListAPIView(APIView):
    permission_classes = (IsAuthenticated,IsAdminUser)
    def get(self, request):
        categorieEs = CategorieEquipement.objects.all()  
        serializer = CategorieEquipementSerializer(categorieEs, many=True)
        
        return Response(serializer.data,status=status.HTTP_200_OK) 

#Classe pour créer une categorie d'équipement 
class CategorieECreateAPIView(APIView):
    permission_classes = (IsAuthenticated,IsAdminUser)
    def post(self, request):
        admin= request.user
        serializer = CategorieEquipementSerializer(data=request.data)  
        if serializer.is_valid():  
            categorieE=serializer.save() 
            InfoSecurite.objects.create(utilisateur=admin,action="créer",type_objet="catégorie Equipement",object_id=categorieE.id) 
            return Response(serializer.data, status=status.HTTP_201_CREATED)  

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


#Classe pour modifier une categorie d'équipement 
class CategorieEUpdateAPIView(APIView):
    permission_classes = (IsAuthenticated,IsAdminUser)
    def put(self, request, categorieE_id):
        admin= request.user
        try:
            categorieE = CategorieEquipement.objects.get(pk=categorieE_id)
        except CategorieEquipement.DoesNotExist:
            return Response({"error": "Cette catégorie d'équipement n'existe pas."}, status=status.HTTP_404_NOT_FOUND)

        serializer = CategorieEquipementSerializer(categorieE , data=request.data)

        if serializer.is_valid():
            serializer.save()
            InfoSecurite.objects.create(utilisateur=admin,action="update",type_objet="catégorie Equipement",object_id=categorieE.id) 
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Classe pour supprimer une categorie d'équipement 
class CategorieEDeleteAPIView(APIView):
    permission_classes = (IsAuthenticated,IsAdminUser)
    def delete(self, request, categorieE_id):
        admin= request.user
        try:
            categorieE = CategorieEquipement.objects.get(pk=categorieE_id)
        except CategorieEquipement.DoesNotExist:
            return Response({"error": "La marque spécifiée n'existe pas."}, status=status.HTTP_404_NOT_FOUND)
        InfoSecurite.objects.create(utilisateur=admin,action="delete",type_objet="catégorie Equipement",object_id=categorieE.id) 
        categorieE.delete()
        return Response({"success": "La marque a été supprimée avec succès."}, status=status.HTTP_204_NO_CONTENT)

#*****************************************************************
#Classe pour lister toutes les categorie d'article 
class CategorieAListAPIView(APIView):
    permission_classes = (IsAuthenticated,IsAdminUser)
    def get(self, request):
        categorieAs = CategorieArticle.objects.all()  
        serializer = CategorieArticleSerializer(categorieAs, many=True)
        
        return Response(serializer.data,status=status.HTTP_200_OK) 

#Classe pour créer une categorie d'article 
class CategorieACreateAPIView(APIView):
    permission_classes = (IsAuthenticated,IsAdminUser)
    def post(self, request):
        admin= request.user
        serializer = CategorieArticleSerializer(data=request.data)  
        if serializer.is_valid():  
            categorieA=serializer.save()  
            InfoSecurite.objects.create(utilisateur=admin,action="créer",type_objet="catégorie Article",object_id=categorieA.id) 
            return Response(serializer.data, status=status.HTTP_201_CREATED)  

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


#Classe pour modifier une categorie d'article 
class CategorieAUpdateAPIView(APIView):
    permission_classes = (IsAuthenticated,IsAdminUser)
    def put(self, request, categorieA_id):
        admin= request.user
        try:
            categorieA = CategorieArticle.objects.get(pk=categorieA_id)
        except CategorieArticle.DoesNotExist:
            return Response({"error": "Cette catégorie d'article n'existe pas."}, status=status.HTTP_404_NOT_FOUND)

        serializer = CategorieArticleSerializer(categorieA , data=request.data)

        if serializer.is_valid():
            serializer.save()
            InfoSecurite.objects.create(utilisateur=admin,action="update",type_objet="catégorie Article",object_id=categorieA.id) 
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Classe pour supprimer une categorie d'article 
class CategorieADeleteAPIView(APIView):
    permission_classes = (IsAuthenticated,IsAdminUser)
    def delete(self, request, categorieA_id):
        admin= request.user
        try:
            categorieA = CategorieArticle.objects.get(pk=categorieA_id)
        except CategorieArticle.DoesNotExist:
            return Response({"error": "La catégorie d'article spécifiée n'existe pas."}, status=status.HTTP_404_NOT_FOUND)

        InfoSecurite.objects.create(utilisateur=admin,action="delete",type_objet="catégorie Article",object_id=categorieA.id) 
        categorieA.delete()
        return Response({"success": "La catégorie d'article a été supprimée avec succès."}, status=status.HTTP_204_NO_CONTENT)


#*****************************************************************
#Classe pour lister toutes les séries 
class SerieListAPIView(APIView):
    permission_classes = (IsAuthenticated,IsAdminUser)
    def get(self, request):
        series = Serie.objects.all()  
        serializer = SerieSerializer(series, many=True)
        
        return Response(serializer.data,status=status.HTTP_200_OK) 

#Classe pour créer une série
class SerieCreateAPIView(APIView):
    permission_classes = (IsAuthenticated,IsAdminUser)
    def post(self, request):
        admin= request.user
        serializer = SerieSerializer(data=request.data)  
        if serializer.is_valid():  
            serie=serializer.save()
            InfoSecurite.objects.create(utilisateur=admin,action="créer",type_objet="série",object_id=serie.id)   
            return Response(serializer.data, status=status.HTTP_201_CREATED)  

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


#Classe pour modifier une série
class SerieUpdateAPIView(APIView):
    permission_classes = (IsAuthenticated,IsAdminUser)
    def put(self, request, serie_id):
        admin= request.user
        try:
            serie = Serie.objects.get(pk=serie_id)
        except Serie.DoesNotExist:
            return Response({"error": "Cette série n'existe pas."}, status=status.HTTP_404_NOT_FOUND)

        serializer = SerieSerializer(serie , data=request.data)

        if serializer.is_valid():
            serializer.save()
            InfoSecurite.objects.create(utilisateur=admin,action="update",type_objet="série",object_id=serie.id)   
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Classe pour supprimer une série 
class SerieDeleteAPIView(APIView):
    permission_classes = (IsAuthenticated,IsAdminUser)
    def delete(self, request, serie_id):
        admin= request.user
        try:
            serie = Serie.objects.get(pk=serie_id)
        except Serie.DoesNotExist:
            return Response({"error": "La série spécifiée n'existe pas."}, status=status.HTTP_404_NOT_FOUND)
        InfoSecurite.objects.create(utilisateur=admin,action="delete",type_objet="série",object_id=serie.id)   
        serie.delete()
        return Response({"success": "La série a été supprimée avec succès."}, status=status.HTTP_204_NO_CONTENT)

#*********************************************************************************
#Classe pour lister toutes les marques
class MarqueListAPIView(APIView):
    permission_classes = (IsAuthenticated,IsAdminUser)
    def get(self, request):
        marques = Marque.objects.all()  
        serializer = MarqueSerializer(marques, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK) 

#Classe pour créer une marque 
class MarqueCreateAPIView(APIView):
    permission_classes = (IsAuthenticated,IsAdminUser)
    def post(self, request):
        admin= request.user
        serializer = MarqueSerializer(data=request.data)  
        if serializer.is_valid():  
            marque=serializer.save() 
            InfoSecurite.objects.create(utilisateur=admin,action="créer",type_objet="marque",object_id=marque.id)    
            return Response(serializer.data, status=status.HTTP_201_CREATED)  

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

#Classe pour modifier une marque
class MarqueUpdateAPIView(APIView):
    permission_classes = (IsAuthenticated,IsAdminUser)
    def put(self, request, marque_id):
        admin= request.user
        try:
            marque = Marque.objects.get(pk=marque_id)
        except Marque.DoesNotExist:
            return Response({"error": "Cette marque n'existe pas."}, status=status.HTTP_404_NOT_FOUND)

        serializer = MarqueSerializer(marque , data=request.data)

        if serializer.is_valid():
            serializer.save()
            InfoSecurite.objects.create(utilisateur=admin,action="update",type_objet="marque",object_id=marque.id) 
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Classe pour supprimer une marque 
class MarqueDeleteAPIView(APIView):
    permission_classes = (IsAuthenticated,IsAdminUser)
    def delete(self, request, marque_id):
        admin= request.user
        try:
            marque = Marque.objects.get(pk=marque_id)
        except Marque.DoesNotExist:
            return Response({"error": "La marque spécifiée n'existe pas."}, status=status.HTTP_404_NOT_FOUND)

        InfoSecurite.objects.create(utilisateur=admin,action="delete",type_objet="marque",object_id=marque.id) 
        marque.delete()
        return Response({"success": "La marque a été supprimée avec succès."}, status=status.HTTP_204_NO_CONTENT)


#****************************************************************************
#Classe pour lister tous les modeles
class ModeleListAPIView(APIView):
    permission_classes = (IsAuthenticated,IsAdminUser)
    def get(self, request):
        modeles = Model.objects.all()  
        serializer = ModelSerializer(modeles, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK) 

#Classe pour créer un modele 
class ModeleCreateAPIView(APIView):
    permission_classes = (IsAuthenticated,IsAdminUser)
    def post(self, request):
        admin= request.user
        serializer = ModelSerializer(data=request.data)  
        if serializer.is_valid():  
            model=serializer.save()  
            InfoSecurite.objects.create(utilisateur=admin,action="créer",type_objet="model",object_id=model.id) 
            return Response(serializer.data, status=status.HTTP_201_CREATED)  

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


#Classe pour modifier les informations d'un modèle
class ModeleUpdateAPIView(APIView):
    permission_classes = (IsAuthenticated,IsAdminUser)
    def put(self, request, modele_id):
        admin= request.user
        try:
            modele = Model.objects.get(pk=modele_id)
        except Modele.DoesNotExist:
            return Response({"error": "Ce modele n'existe pas."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ModelSerializer(modele, data=request.data)

        if serializer.is_valid():
            serializer.save()
            InfoSecurite.objects.create(utilisateur=admin,action="update",type_objet="model",object_id=modele.id) 
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Classe pour supprimer un modele 
class ModeleDeleteAPIView(APIView):
    permission_classes = (IsAuthenticated,IsAdminUser)
    def delete(self, request, modele_id):
        admin= request.user
        try:   
            modele = Model.objects.get(pk=modele_id)
        except Model.DoesNotExist:
            return Response({"error": "Le modele spécifiée n'existe pas."}, status=status.HTTP_404_NOT_FOUND)

        InfoSecurite.objects.create(utilisateur=admin,action="créer",type_objet="model",object_id=modele.id) 
        modele.delete()
        return Response({"success": "Le modele a été supprimée avec succès."}, status=status.HTTP_204_NO_CONTENT)           


#****************************************************************************
#Classe pour lister tous les stocks
class StockListAPIView(APIView):
    permission_classes = (IsAuthenticated,IsAdminUser)
    def get(self, request):
        stocks = Stock.objects.all()  
        serializer = StockSerializer(stocks, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK) 


#Classe pour supprimer un stock 
class StockDeleteAPIView(APIView):
    permission_classes = (IsAuthenticated,IsAdminUser)
    def delete(self, request, stock_id):
        admin= request.user
        try:   
            stock = Stock.objects.get(pk=stock_id)
        except Stock.DoesNotExist:
            return Response({"error": "Le stock spécifiée n'existe pas."}, status=status.HTTP_404_NOT_FOUND)
        InfoSecurite.objects.create(utilisateur=admin,action="delete",type_objet="stock",object_id=stock.id) 
        stock.delete()
        return Response({"success": "Le stock a été supprimée avec succès."}, status=status.HTTP_204_NO_CONTENT)           


#****************************************************************************
#Classe pour enregistrer un switch
class SwitchCreateAPIView(APIView):
    permission_classes = (IsAuthenticated,IsAdminUser)
    def post(self,request):
       
        serializer = SwitchSerializer(data=request.data)  
        
        if serializer.is_valid(): 
            quantite_article = serializer.validated_data.get('quantite_article', 0)
            prix = serializer.validated_data.get('prix', 0)

            if quantite_article > 0 and prix > 0:
                admin= request.user
                switch=serializer.save(admin=admin)  

                statut_stock = "En stock"
                quantite_article_stock=switch.quantite_article
                stock = Stock.objects.create(quantite_article=quantite_article_stock,statut=statut_stock)
                switch.stock=stock
                switch.save()
                InfoSecurite.objects.create(utilisateur=admin,action="créer",type_objet="switch",object_id=switch.id)
                return Response(serializer.data, status=status.HTTP_201_CREATED)  

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

#***********************************************************************************
#Classe pour lister toutes les promotions
class PromotionListAPIView(APIView):
    permission_classes = (IsAuthenticated,IsAdminUser)
    def get(self, request):
        promotions = Promotion.objects.all()  
        serializer = PromotionSerializer(promotions, many=True)
        
        return Response(serializer.data,status=status.HTTP_200_OK) 

#Classe pour créer une promotion 
class PromotionCreateAPIView(APIView):
    permission_classes = (IsAuthenticated,IsAdminUser)
    def post(self, request):
        admin= request.user
        serializer = PromotionSerializer(data=request.data) 
        date_debut = request.data.get('date_debut')
        date_fin = request.data.get('date_fin')

        if date_debut >= date_fin:
            return Response(
                {"error": "La date de debut doit être inférieure à la date de fin."},
                status=status.HTTP_400_BAD_REQUEST
            )
         
        if serializer.is_valid():  
            promotion=serializer.save() 
            InfoSecurite.objects.create(utilisateur=admin,action="créer",type_objet="promotion",object_id=promotion.id) 
            return Response(serializer.data, status=status.HTTP_201_CREATED)  

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


#Classe pour modifier une promotion
class PromotionUpdateAPIView(APIView):
    permission_classes = (IsAuthenticated,IsAdminUser)
    def put(self, request, promotion_id):
        admin= request.user
        try:
            promotion = Promotion.objects.get(pk=promotion_id)
        except Promotion.DoesNotExist:
            return Response({"error": "Cette promotion n'existe pas."}, status=status.HTTP_404_NOT_FOUND)

        serializer = PromotionSerializer(promotion , data=request.data)

        date_debut = request.data.get('date_debut')
        date_fin = request.data.get('date_fin')

        if date_debut >= date_fin:
            return Response(
                {"error": "La date de debut doit être inférieure à la date de fin."},
                status=status.HTTP_400_BAD_REQUEST
            )
        if serializer.is_valid():
            serializer.save()
            InfoSecurite.objects.create(utilisateur=admin,action="update",type_objet="promotion",object_id=promotion.id) 
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Classe pour supprimer une promotion
class PromotionDeleteAPIView(APIView):
    permission_classes = (IsAuthenticated,IsAdminUser)
    def delete(self, request, promotion_id):
        admin= request.user
        try:
            promotion = Promotion.objects.get(pk=promotion_id)
        except Promotion.DoesNotExist:
            return Response({"error": "La promotion spécifiée n'existe pas."}, status=status.HTTP_404_NOT_FOUND)
        InfoSecurite.objects.create(utilisateur=admin,action="delete",type_objet="promotion",object_id=promotion.id) 
        promotion .delete()
        return Response({"success": "La promotion a été supprimée avec succès."}, status=status.HTTP_204_NO_CONTENT)

#***********************************************************************************
#Classe pour assigné une promotion à un article
class PromotionArticleCreateAPIView(APIView):
    permission_classes = (IsAuthenticated,IsAdminUser)
    def post(self, request):
        admin= request.user
        serializer = PromotionArticleSerializer(data=request.data)  

        if serializer.is_valid():
            article_id = request.data.get('article')
            promo = request.data.get('promotion')
            produit_deja_en_promo = PromotionArticle.objects.filter(
                article=article_id,
                promotion__statut=False
            ).first()

            promo_choisi = Promotion.objects.filter(
                id=promo
            ).first()


            if produit_deja_en_promo:
                return Response("cet article à déjà une promotion en cours", status=status.HTTP_400_BAD_REQUEST)
            
            if promo_choisi.statut == True:
                return Response("la promotion choisi est déjà terminé", status=status.HTTP_400_BAD_REQUEST)
	    
            promotion_article = serializer.save()
            InfoSecurite.objects.create(
                    utilisateur=admin,
                    action="créer",
                    type_objet="promotion_article",
                    object_id=promotion_article.id
                    )
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
