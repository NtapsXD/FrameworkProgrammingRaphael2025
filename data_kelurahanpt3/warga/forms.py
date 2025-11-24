from django import forms
from .models import Warga, Pengaduan

# FORM 1: Untuk Input Warga (Materi Praktikum)
class WargaForm(forms.ModelForm):
    class Meta:
        model = Warga
        fields = ['nik', 'nama_lengkap', 'alamat', 'no_telepon']

# FORM 2: Untuk Input Pengaduan (Tugas Challenge)
class PengaduanForm(forms.ModelForm):
    class Meta:
        model = Pengaduan
        fields = ['judul', 'deskripsi', 'status', 'pelapor']