from django.shortcuts import render
from rest_framework.views import APIView  
from rest_framework import status  
from rest_framework.response import Response  
from produit.models import *  
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
        serializer = CategorieEquipementSerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)  

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


#Classe pour modifier une categorie d'équipement 
class CategorieEUpdateAPIView(APIView):
    permission_classes = (IsAuthenticated,IsAdminUser)
    def put(self, request, categorieE_id):
        try:
            categorieE = CategorieEquipement.objects.get(pk=categorieE_id)
        except CategorieEquipement.DoesNotExist:
            return Response({"error": "Cette catégorie d'équipement n'existe pas."}, status=status.HTTP_404_NOT_FOUND)

        serializer = CategorieEquipementSerializer(categorieE , data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Classe pour supprimer une categorie d'équipement 
class CategorieEDeleteAPIView(APIView):
    permission_classes = (IsAuthenticated,IsAdminUser)
    def delete(self, request, categorieE_id):
        try:
            categorieE = CategorieEquipement.objects.get(pk=categorieE_id)
        except CategorieEquipement.DoesNotExist:
            return Response({"error": "La marque spécifiée n'existe pas."}, status=status.HTTP_404_NOT_FOUND)

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
        serializer = CategorieArticleSerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)  

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


#Classe pour modifier une categorie d'article 
class CategorieAUpdateAPIView(APIView):
    permission_classes = (IsAuthenticated,IsAdminUser)
    def put(self, request, categorieA_id):
        try:
            categorieA = CategorieArticle.objects.get(pk=categorieA_id)
        except CategorieArticle.DoesNotExist:
            return Response({"error": "Cette catégorie d'article n'existe pas."}, status=status.HTTP_404_NOT_FOUND)

        serializer = CategorieArticleSerializer(categorieA , data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Classe pour supprimer une categorie d'article 
class CategorieADeleteAPIView(APIView):
    permission_classes = (IsAuthenticated,IsAdminUser)
    def delete(self, request, categorieA_id):
        try:
            categorieA = CategorieArticle.objects.get(pk=categorieA_id)
        except CategorieArticle.DoesNotExist:
            return Response({"error": "La catégorie d'article spécifiée n'existe pas."}, status=status.HTTP_404_NOT_FOUND)

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
        serializer = SerieSerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)  

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


#Classe pour modifier une série
class SerieUpdateAPIView(APIView):
    permission_classes = (IsAuthenticated,IsAdminUser)
    def put(self, request, serie_id):
        try:
            serie = Serie.objects.get(pk=serie_id)
        except Serie.DoesNotExist:
            return Response({"error": "Cette série n'existe pas."}, status=status.HTTP_404_NOT_FOUND)

        serializer = SerieSerializer(serie , data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Classe pour supprimer une série 
class SerieDeleteAPIView(APIView):
    permission_classes = (IsAuthenticated,IsAdminUser)
    def delete(self, request, serie_id):
        try:
            serie = Serie.objects.get(pk=serie_id)
        except Serie.DoesNotExist:
            return Response({"error": "La série spécifiée n'existe pas."}, status=status.HTTP_404_NOT_FOUND)

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
        serializer = MarqueSerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)  

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

#Classe pour modifier une marque
class MarqueUpdateAPIView(APIView):
    permission_classes = (IsAuthenticated,IsAdminUser)
    def put(self, request, marque_id):
        try:
            marque = Marque.objects.get(pk=marque_id)
        except Marque.DoesNotExist:
            return Response({"error": "Cette marque n'existe pas."}, status=status.HTTP_404_NOT_FOUND)

        serializer = MarqueSerializer(marque , data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Classe pour supprimer une marque 
class MarqueDeleteAPIView(APIView):
    permission_classes = (IsAuthenticated,IsAdminUser)
    def delete(self, request, marque_id):
        try:
            marque = Marque.objects.get(pk=marque_id)
        except Marque.DoesNotExist:
            return Response({"error": "La marque spécifiée n'existe pas."}, status=status.HTTP_404_NOT_FOUND)

        marque.delete()
        return Response({"success": "La marque a été supprimée avec succès."}, status=status.HTTP_204_NO_CONTENT)


#****************************************************************************
#Classe pour lister tous les modeles
class ModeleListAPIView(APIView):
    permission_classes = (IsAuthenticated,IsAdminUser)
    def get(self, request):
        modeles = Modele.objects.all()  
        serializer = ModeleResponseSerializer(modeles, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK) 

#Classe pour créer un modele 
class ModeleCreateAPIView(APIView):
    permission_classes = (IsAuthenticated,IsAdminUser)
    def post(self, request):
        serializer = MarqueSerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)  

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


#Classe pour modifier les informations d'un modèle
class ModeleUpdateAPIView(APIView):
    permission_classes = (IsAuthenticated,IsAdminUser)
    def put(self, request, modele_id):
        try:
            modele = Modele.objects.get(pk=modele_id)
        except Modele.DoesNotExist:
            return Response({"error": "Ce modele n'existe pas."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ModeleSerializer(modele, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Classe pour supprimer un modele 
class ModeleDeleteAPIView(APIView):
    permission_classes = (IsAuthenticated,IsAdminUser)
    def delete(self, request, modele_id):
        try:   
            modele = Modele.objects.get(pk=modele_id)
        except Modele.DoesNotExist:
            return Response({"error": "Le modele spécifiée n'existe pas."}, status=status.HTTP_404_NOT_FOUND)

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
        try:   
            stock = Stock.objects.get(pk=stock_id)
        except Stock.DoesNotExist:
            return Response({"error": "Le stock spécifiée n'existe pas."}, status=status.HTTP_404_NOT_FOUND)

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
                print(isinstance(admin,UtilisateurPersonalisee))
                switch=serializer.save(admin=admin)  

                statut_stock = "En stock"
                quantite_article_stock=switch.quantite_article
                stock = Stock.objects.create(quantite_article=quantite_article_stock,statut=statut_stock)
                switch.stock=stock
                switch.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)  

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  