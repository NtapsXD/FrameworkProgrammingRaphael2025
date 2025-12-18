from django.contrib import admin
from .models import Warga, Pengaduan

class WargaAdmin(admin.ModelAdmin):
    list_display = ('nama_lengkap', 'nik', 'no_telepon')

class PengaduanAdmin(admin.ModelAdmin):
    # Gunakan 'pelapor' (sesuai models.py) dan 'tanggal_lapor' (sesuai models.py)
    list_display = ('judul', 'pelapor', 'status', 'tanggal_lapor') 
    list_filter = ('status',)

admin.site.register(Warga, WargaAdmin)
admin.site.register(Pengaduan, PengaduanAdmin)