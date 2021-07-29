from rest_framework import serializers
from main.models import Suco

class SucoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suco
        fields = ('nome', 'litros', 'link', 'qtd_disp')
