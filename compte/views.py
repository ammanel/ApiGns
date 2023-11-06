from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from knox.auth import AuthToken
from django.contrib.auth import authenticate,get_user_model, login
from compte.serializers import  *
from rest_framework import status  
from knox.views import LoginView 
from rest_framework.exceptions import AuthenticationFailed
from knox import views as knox_views
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView  
from compte.models import Role



#fonction de connexion
class LoginAPIView(knox_views.LoginView):
    permission_classes = (AllowAny,)
    serializer_class = ConnexionSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            login(request, user)
            response = super().post(request, format=None)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        return Response(response.data, status=status.HTTP_200_OK)
    
#récuper les données de l'utilisateur a partir du token
@api_view(['GET'])
def recuperer_les_donnees_utilisateur(request):
    user= request.user
    if user.is_authenticated:

        return Response(
            {
                'user_info':{
                    'id':user.id,
                    'nom':user.nom,
                    'prenom':user.prenom,
                    'email':user.email
                }
            }
        )
    return Response({'error':'connectez-vous'}, status=400)

#inscription du client
@api_view(['POST'])
def inscriptionClient(request):
    serializer = ClientSerializer(data=request.data)  
    if serializer.is_valid(raise_exception=True):  
            user=serializer.save()  
            role_client, _ = Role.objects.get_or_create(libelle='ROLE_CLIENT',code='001')
            user.role=role_client
            user.is_active=True
            password = request.data.get('password')
            user.set_password(password)
            user.save()

            _,token=AuthToken.objects.create(user)
            user_info={
                'id':user.id,
                'email':user.email,
                'nom':user.nom,
                'prenom':user.prenom,
                'role':user.role.libelle
            }
            return Response({'user_info': user_info, 'token': token})  

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

#inscription de l'Admin
@api_view(['POST'])
def inscriptionAdmin(request):
    User = get_user_model()
    data = request.data.copy()
    data['is_staff'] = True
    data['is_superuser'] = True 
    serializer = AdminSerializer(data=data) 

    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        role_admin, _ = Role.objects.get_or_create(libelle='ROLE_ADMIN',code='002')
        user.role=role_admin
        user.is_active=True
        password = request.data.get('password')
        user.set_password(data['password'])  
        user.save() 
        _,token=AuthToken.objects.create(user)

        user_info = {
            'id': user.id,
            'email': user.email,
            'nom': user.nom,
            'prenom': user.prenom,
            'role': user.role.libelle
        }
        
        return Response({'user_info': user_info, 'token': token})
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#créer un role
class RoleCreateAPIView(APIView):
    def post(self, request):
        serializer = RoleSerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)  

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

#Classe pour lister tous les roles
class RoleListAPIView(APIView):
   
    def get(self, request):
        roles = Role.objects.all()  
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 


#Classe pour modifier un role
class RoleUpdateAPIView(APIView):
    def put(self, request, role_id):
        try:
            role = Role.objects.get(pk=role_id)
        except  Role.DoesNotExist:
            return Response({"error": "ce role n'existe pas."}, status=status.HTTP_404_NOT_FOUND)

        serializer = RoleSerializer(role , data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Classe pour supprimer un role 
class RoleDeleteAPIView(APIView):

     def delete(self, request, role_id):
        try:
            role = Role.objects.get(pk=role_id)
        except Role.DoesNotExist:
            return Response({"error": "Le role spécifiée n'existe pas."}, status=status.HTTP_404_NOT_FOUND)

        role.delete()
        return Response({"success": "Le role a été supprimée avec succès."}, status=status.HTTP_204_NO_CONTENT)

