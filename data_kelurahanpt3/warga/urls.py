from django.urls import path
# Import view baru: WargaCreateView dan PengaduanCreateView
from .views import WargaListView, WargaDetailView, PengaduanListView, WargaCreateView, PengaduanCreateView

urlpatterns = [
    # URL Warga
    path('', WargaListView.as_view(), name='warga-list'),
    path('tambah/', WargaCreateView.as_view(), name='warga-tambah'), # URL Baru
    path('<int:pk>/', WargaDetailView.as_view(), name='warga-detail'),
    
    # URL Pengaduan
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan-list'),
    path('pengaduan/tambah/', PengaduanCreateView.as_view(), name='pengaduan-tambah'), # URL Challenge
]