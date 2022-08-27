from rest_framework import serializers
from mobapi.models import Mobiles

class MobileSerializers(serializers.Serializer):
    id=serializers.CharField(read_only=True)
    name=serializers.CharField()
    brand=serializers.CharField()
    display=serializers.CharField()
    band=serializers.CharField()
    price=serializers.IntegerField()

class MobileModelSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Mobiles
        fields="__all__"