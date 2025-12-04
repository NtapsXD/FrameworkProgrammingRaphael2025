from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny, IsAdminUser
from .models import Warga, Pengaduan
from .serializers import WargaSerializer, PengaduanSerializer

# ViewSet otomatis menangani: List, Create, Retrieve, Update, Delete

class WargaViewSet(viewsets.ModelViewSet):
    """
    API endpoint untuk mengelola data Warga.
    """
    # Menggunakan order_by('-id') agar data terbaru muncul paling atas
    queryset = Warga.objects.all().order_by('-id')
    serializer_class = WargaSerializer
    permission_classes = [IsAdminUser]

class PengaduanViewSet(viewsets.ModelViewSet):
    """
    API endpoint untuk mengelola data Pengaduan.
    """
    queryset = Pengaduan.objects.all().order_by('-id')
    serializer_class = PengaduanSerializer
    #permission_classes = [IsAuthenticated]