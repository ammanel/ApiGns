from django.urls import path
from . import views

urlpatterns = [
    path('enregistrer/switch', views.SwitchCreateAPIView.as_view(), name='creer_switch'),
   
   
]
