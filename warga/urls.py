from django.urls import path
# Import View untuk HTML (bukan API)
from .views import (
    WargaListView, WargaDetailView, WargaCreateView, WargaUpdateView, WargaDeleteView,
    PengaduanListView, PengaduanCreateView, PengaduanUpdateView, PengaduanDeleteView
)

urlpatterns = [
    # --- URL Aplikasi Web (HTML) ---
    
    # Warga
    path('', WargaListView.as_view(), name='warga-list'),
    path('tambah/', WargaCreateView.as_view(), name='warga-tambah'),
    path('<int:pk>/', WargaDetailView.as_view(), name='warga-detail'),
    path('<int:pk>/edit/', WargaUpdateView.as_view(), name='warga-edit'),
    path('<int:pk>/hapus/', WargaDeleteView.as_view(), name='warga-hapus'),

    # Pengaduan
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan-list'),
    path('pengaduan/tambah/', PengaduanCreateView.as_view(), name='pengaduan-tambah'),
    path('pengaduan/<int:pk>/edit/', PengaduanUpdateView.as_view(), name='pengaduan-edit'),
    path('pengaduan/<int:pk>/hapus/', PengaduanDeleteView.as_view(), name='pengaduan-hapus'),
]