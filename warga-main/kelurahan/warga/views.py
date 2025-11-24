from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView
from .serializers import WargaSerializer, PengaduanSerializer
from .models import Warga, Pengaduan
# Create your views here.

class WargaListAPIView(ListAPIView):
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer

class PengaduanListCreateAPIView(ListCreateAPIView):
    queryset = Pengaduan.objects.all()
    serializer_class = PengaduanSerializer