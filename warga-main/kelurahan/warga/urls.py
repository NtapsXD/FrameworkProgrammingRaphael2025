from django.urls import path
from .views import WargaListAPIView, PengaduanListCreateAPIView

urlpatterns = [
    path('', WargaListAPIView.as_view(), name='warga-list'),
    path('pengaduan/', PengaduanListCreateAPIView.as_view(), name='pengaduan-list'),
]