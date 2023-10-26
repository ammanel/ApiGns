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
    
    class Meta:
        model = Article
        fields=('categorie_article','model','nom','prix','description','quantite_article','image_principale')

        
    
        
class SwitchSerializer(ArticleSerializer):
    
    class Meta:
        model = Switch
        fields =  '__all__'

    #logique pour permettre à un switch d'avoir plusieurs images
    images = ImageArticleSerializer(many=True, required=False,read_only=True)
    images_telecharger=serializers.ListField(
        child=serializers.ImageField(max_length=1000000,allow_empty_file=False,use_url=False),
        write_only=True
    )
    def create(self,validated_data):
        images_telecharger=validated_data.pop("images_telecharger")
        article=Switch.objects.create(**validated_data)
        for image in images_telecharger:
            ImageArticle.objects.create(article=article,image=image)
        return article

class RouteurSerializer(ArticleSerializer):
    class Meta:
        model = Routeur
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