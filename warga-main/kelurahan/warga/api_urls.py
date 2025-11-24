# warga/api_urls.py
from django.urls import path
from .views import WargaListAPIView, PengaduanListCreateAPIView

urlpatterns = [
    path('warga/', WargaListAPIView.as_view(),name='api-warga-list'),
    path('pengaduan/', PengaduanListCreateAPIView.as_view(), name='api-pengaduan-list-create'),
]