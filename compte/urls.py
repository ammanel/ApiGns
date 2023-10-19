from django.urls import path
from . import views
from knox.views import LogoutView,LogoutAllView

urlpatterns = [
    path('connexion', views.LoginAPIView.as_view(), name='connexion'),
    path('utilisateur/donnee',views.recuperer_les_donnees_utilisateur, name='utilisateur_detail'),
    path('inscription/client',views.inscriptionClient, name='inscription_client'),
    path('inscription/admin',views.inscriptionAdmin, name='inscription_admin'),
    path('deconnexion',LogoutView.as_view(), name='deconnexion'),
    path('creation/role',views.RoleCreateAPIView.as_view(), name='creation_role'),
    path('update/role/<int:role_id>',views.RoleUpdateAPIView.as_view(), name='update_role'),
    path('delete/role/<int:role_id>',views.RoleDeleteAPIView.as_view(), name='delete_role'),
    path('list/role',views.RoleListAPIView.as_view(), name='list_role'),
   
]
