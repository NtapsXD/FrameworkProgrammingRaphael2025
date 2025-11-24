from rest_framework import serializers
from .models import Warga, Pengaduan

class WargaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warga
        fields = ['id','nik','nama_lengkap','alamat','no_telepon']

class PengaduanSerializer(serializers.ModelSerializer):
    warga_nama = serializers.CharField(source='warga.nama_lengkap', read_only=True)

    class Meta:
        model = Pengaduan
        fields = ['id', 'warga', 'warga_nama', 'judul', 'isi_laporan', 'tanggal', 'status']