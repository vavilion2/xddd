from dungeon.models import Zayavka
from .serializers import ZayavkaSerializer
from rest_framework import generics
from rest_framework.filters import SearchFilter


class ZayavkaApiList(generics.ListAPIView):
    queryset = Zayavka.objects.all()
    serializer_class = ZayavkaSerializer
    filter_backends = [SearchFilter]
    search_fields=['user__username','tip__tip_rabot']






#class ZayavkaRList(generics.ListCreateAPIView):
#    queryset = Zayavka.objects.all()
#    serializer_class = ZayavkaSerializer
#
#
#class ZayavkaRDetail(generics.RetrieveUpdateDestroyAPIView):
#    queryset = Zayavka.objects.all()
#    serializer_class = ZayavkaSerializer