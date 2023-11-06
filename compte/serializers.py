from compte.models import UtilisateurPersonalisee,Role,Admin,Client
from django.contrib.auth import authenticate
from rest_framework import serializers


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class UtilisateurPersonaliseeSerializer(serializers.ModelSerializer):
    class Meta:
        model=UtilisateurPersonalisee
        fields=('password','email','nom','prenom')
        extra_kwargs = {
            'password': {'write_only': True}
        }

class AdminSerializer(UtilisateurPersonaliseeSerializer):
    class Meta:
        model = Admin
        fields = '__all__'
        


class ClientSerializer(UtilisateurPersonaliseeSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ConnexionSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, attrs):
        email = attrs.get('email').lower()
        password = attrs.get('password')

        if not email or not password:
            raise serializers.ValidationError("Entrer votre mot de passe et votre email.")

        if not UtilisateurPersonalisee.objects.filter(email=email).exists():
            raise serializers.ValidationError('cet email n\'existe pas.')

        user = authenticate(request=self.context.get('request'), email=email,password=password)
        if not user:
            raise serializers.ValidationError("Données erronnées.")

        attrs['user'] = user
        return attrs