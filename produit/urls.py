from django.urls import path
from . import views

urlpatterns = [
    path('enregistrer/switch', views.SwitchCreateAPIView.as_view(), name='creer_switch'),

    path('enregistrer/categorie/Equipement', views.CategorieECreateAPIView.as_view(), name='creer_cat_equipement'),
    path('liste/categorie/Equipement', views.CategorieEListAPIView.as_view(), name='creer_cat_equipement'),
    path('update/categorie/Equipement/<int:categorieE_id>', views.CategorieEUpdateAPIView.as_view(), name='update_cat_equipement'),
    path('delete/categorie/Equipement/<int:categorieE_id>', views.CategorieEDeleteAPIView.as_view(), name='delete_cat_equipement'),

    path('enregistrer/categorie/Article', views.CategorieACreateAPIView.as_view(), name='creer_cat_article'),
    path('liste/categorie/Article', views.CategorieAListAPIView.as_view(), name='liste_cat_article'),
    path('update/categorie/Article/<int:categorieA_id>', views.CategorieAUpdateAPIView.as_view(), name='update_cat_article'),
    path('delete/categorie/Article/<int:categorieA_id>', views.CategorieADeleteAPIView.as_view(), name='delete_cat_article'),

    path('enregistrer/serie', views.SerieCreateAPIView.as_view(), name='creer_serie'),
    path('liste/serie', views.SerieListAPIView.as_view(), name='liste_serie'),
    path('update/serie/<int:serie_id>', views.SerieUpdateAPIView.as_view(), name='update_serie'),
    path('delete/serie/<int:serie_id>', views.SerieDeleteAPIView.as_view(), name='delete_serie'),

    path('enregistrer/marque', views.MarqueCreateAPIView.as_view(), name='creer_marque'),
    path('liste/marque', views.MarqueListAPIView.as_view(), name='liste_marque'),
    path('update/marque/<int:marque_id>', views.MarqueUpdateAPIView.as_view(), name='update_marque'),
    path('delete/marque/<int:marque_id>', views.MarqueDeleteAPIView.as_view(), name='delete_marque'),

    path('enregistrer/modele', views.ModeleCreateAPIView.as_view(), name='creer_modele'),
    path('liste/modele', views.ModeleListAPIView.as_view(), name='liste_modele'),
    path('update/modele/<int:modele_id>', views.ModeleUpdateAPIView.as_view(), name='update_modele'),
    path('delete/modele/<int:modele_id>', views.ModeleDeleteAPIView.as_view(), name='delete_modele'),

    path('delete/stock/<int:stock_id>', views.StockDeleteAPIView.as_view(), name='delete_stock'),
    path('liste/stock', views.StockListAPIView.as_view(), name='liste_stock'),
   
    path('enregistrer/promotion', views.PromotionCreateAPIView.as_view(), name='creer_promotion'),
    path('liste/promotion', views.PromotionListAPIView.as_view(), name='liste_promotion'),
    path('update/promotion/<int:promotion_id>', views.PromotionUpdateAPIView.as_view(), name='update_promotion'),
    path('delete/promotion/<int:promotion_id>', views.PromotionDeleteAPIView.as_view(), name='delete_promotion'),

    path('enregistrer/promotion/article', views.PromotionArticleCreateAPIView.as_view(), name='creer_promotion_article'),
]
