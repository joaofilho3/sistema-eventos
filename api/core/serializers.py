from rest_framework import serializers
from .models import Evento, Lote, Ingresso

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = "__all__"

class LoteSerializer(serializers.ModelSerializer):
    ingressos_disponiveis = serializers.IntegerField(read_only=True)

    class Meta:
        model = Lote
        fields = "__all__"

class IngressoSerializer(serializers.ModelSerializer):
    comprador = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Ingresso
        fields = "__all__"
        read_only_fields = ["status", "codigo"]

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["comprador"] = request.user
        return super().create(validated_data)
