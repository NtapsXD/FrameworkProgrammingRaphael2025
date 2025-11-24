from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WargaViewSet, PengaduanViewSet

# Membuat Router
router = DefaultRouter()

# Mendaftarkan ViewSet ke Router
# Ini akan menghasilkan URL seperti: /warga/, /warga/{id}/, /pengaduan/, dll.
router.register(r'warga', WargaViewSet, basename='warga')
router.register(r'pengaduan', PengaduanViewSet, basename='pengaduan')

urlpatterns = [
    path('', include(router.urls)),
]