from securite.models import InfoSecurite
from rest_framework import serializers


class InfoSecuriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoSecurite
        fields = '__all__'