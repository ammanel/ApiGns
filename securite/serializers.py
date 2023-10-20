from securite.models import InfoSecurite
from rest_framework import serializers


class InfoSecuriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoInfoSecuritele
        fields = '__all__'