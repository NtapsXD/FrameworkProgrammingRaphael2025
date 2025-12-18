from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny, IsAdminUser
from rest_framework.filters import SearchFilter, OrderingFilter
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
    permission_classes = [AllowAny]

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nama_lengkap', 'nik', 'alamat']
    ordering_fields = ['nama_lengkap', 'tanggal_registrasi', 'id']


class PengaduanViewSet(viewsets.ModelViewSet):
    """
    API endpoint untuk mengelola data Pengaduan.
    """
    queryset = Pengaduan.objects.all().order_by('-id')
    serializer_class = PengaduanSerializer
    permission_classes = [AllowAny]

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['judul', 'deskripsi']
    ordering_fields = ['status', 'tanggal_lapor', 'id']