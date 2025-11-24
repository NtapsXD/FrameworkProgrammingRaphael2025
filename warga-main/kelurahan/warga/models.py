from django.db import models

# Create your models here.
class Warga(models.Model):
    nik = models.CharField(max_length=16, unique=True)
    nama_lengkap = models.CharField(max_length=100)
    alamat = models.TextField()
    no_telepon = models.CharField(max_length=15)

    def __str__(self):
        return self.nama_lengkap

class Pengaduan(models.Model):
    warga = models.ForeignKey(Warga, on_delete=models.CASCADE, related_name='pengaduan')
    judul = models.CharField(max_length=200)
    isi_laporan = models.TextField()
    tanggal = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('baru', 'Baru'),
            ('proses', 'Diproses'),
            ('selesai', 'Selesai'),
        ],
        default='baru'
    )

    def __str__(self):
        return f"{self.judul} - {self.warga.nama_lengkap}"