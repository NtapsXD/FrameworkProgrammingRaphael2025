from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView # Tambah CreateView
from .models import Warga, Pengaduan
from .forms import WargaForm, PengaduanForm # Import form yang baru dibuat

# ... (View ListView dan DetailView yang sudah ada biarkan saja) ...
class WargaListView(ListView):
    model = Warga

class WargaDetailView(DetailView):
    model = Warga

class PengaduanListView(ListView):
    model = Pengaduan

# --- BAGIAN BARU PERTEMUAN 3 ---

# VIEW 1: Tambah Warga (Materi Praktikum)
class WargaCreateView(CreateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list')

# VIEW 2: Tambah Pengaduan (Tugas Challenge)
class PengaduanCreateView(CreateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan-list')