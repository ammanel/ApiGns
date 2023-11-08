from django.urls import path
from . import views
urlpatterns = [
    path('ajouter/panier/<int:id_produit>', views.AjouterAuPanierAPIView.as_view(), name='ajouter_panier'),
    path('delete/article/panier/<int:id_produit>', views.SupprimerDuPanierAPIView.as_view(), name='supp_article_panier'),
    path('valider/panier/<int:id_panier>', views.ValiderUnPanierAPIView.as_view(), name='valider_panier'),
    
]