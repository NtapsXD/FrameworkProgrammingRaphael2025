from django.urls import path
from .views import (
    WargaListView, WargaDetailView, WargaCreateView, 
    WargaUpdateView, WargaDeleteView, # Import baru
    PengaduanListView, PengaduanCreateView,
    PengaduanUpdateView, PengaduanDeleteView # Import baru
)

urlpatterns = [
    # --- URL Warga ---
    path('', WargaListView.as_view(), name='warga-list'),
    path('tambah/', WargaCreateView.as_view(), name='warga-tambah'),
    path('<int:pk>/', WargaDetailView.as_view(), name='warga-detail'),
    
    # URL Edit & Hapus Warga (Pertemuan 4)
    path('<int:pk>/edit/', WargaUpdateView.as_view(), name='warga-edit'),
    path('<int:pk>/hapus/', WargaDeleteView.as_view(), name='warga-hapus'),

    # --- URL Pengaduan ---
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan-list'),
    path('pengaduan/tambah/', PengaduanCreateView.as_view(), name='pengaduan-tambah'),
    
    # URL Edit & Hapus Pengaduan (Challenge Pertemuan 4)
    path('pengaduan/<int:pk>/edit/', PengaduanUpdateView.as_view(), name='pengaduan-edit'),
    path('pengaduan/<int:pk>/hapus/', PengaduanDeleteView.as_view(), name='pengaduan-hapus'),
]