from produit.models import *
from rest_framework import serializers

class CategorieEquipementSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategorieEquipement
        fields = '__all__'

class CategorieArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategorieArticle
        fields = '__all__'

class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = '__all__'

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = '__all__'

class MarqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marque
        fields = '__all__'

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

class ImageArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageArticle
        fields = '__all__'
        

class ArticleSerializer(serializers.ModelSerializer):
    # images = ImageArticleSerializer(many=True, required=False)
    class Meta:
        model = Article
        fields = '__all__'
        

class SwitchSerializer(ArticleSerializer):
    class Meta:
        model = Switch
        fields = '__all__'

class RouteurSerializer(ArticleSerializer):
    class Meta:
        model = Routeur
        fields = '__all__'

class ServerSerializer(ArticleSerializer):
    class Meta:
        model = Server
        fields = '__all__'


class ServerSerializer(ArticleSerializer):
    class Meta:
        model = Server
        fields = '__all__'

class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = '__all__'

class PromotionArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromotionArticle
        fields = '__all__'