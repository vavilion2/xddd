from rest_framework import serializers
from dungeon.models import Zayavka, User,TipRabot

class ZayavkaSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects)
    data = serializers.DateTimeField()
    imya = serializers.CharField()
    familiya = serializers.CharField()

    tip = serializers.PrimaryKeyRelatedField(queryset=TipRabot.objects)
    text = serializers.CharField()
    status = serializers.BooleanField()
    cleent = serializers.PrimaryKeyRelatedField(queryset=User.objects)



    class Meta:
        model = Zayavka
        fields = ('__all__')




#class TipRabotSreializer(ZayavkaSerializer,serializers.ModelSerializer):
#
#    class Meta:
#        model=TipRabot
#        fields = ('__all__')