from django.contrib import admin
from .models import Warga, Pengaduan

# Register your models here.
@admin.register(Warga)
class WargaAdmin(admin.ModelAdmin):
    list_display = ('nik', 'nama_lengkap', 'alamat', 'no_telepon')

@admin.register(Pengaduan)
class PengaduanAdmin(admin.ModelAdmin):
    list_display = ('id', 'warga', 'judul', 'status', 'tanggal')
    list_filter = ('status',)
    search_fields = ('judul', 'isi', 'warga__nama_lengkap')