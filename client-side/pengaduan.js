document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('pengaduan-list-container');
    const apiUrl = 'http://127.0.0.1:8000/api/pengaduan/';

    const token = localStorage.getItem('authToken');
    if (!token) {
        window.location.href = 'index.html';
        return;
    }

    function escapeHtml(str) {
        return String(str ?? '')
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#39;');
    }

    function renderPengaduanCard(p, index) {
        const card = document.createElement('div');
        card.className = 'card mb-3 shadow-sm';
        card.innerHTML = `
            <div class="card-body">
                <h5 class="card-title">${escapeHtml(p.judul || '-')}</h5>
                <p class="card-text mb-1">
                    <small class="text-muted">Pelapor: ${escapeHtml(p.pelapor || '-')}</small>
                </p>
                <p class="card-text mb-1">
                    <small>Status: ${escapeHtml(p.status || '-')}</small>
                </p>
                <p class="card-text mb-2">
                    <small>Tanggal: ${escapeHtml(p.tanggal_lapor || '-')}</small>
                </p>
                <p class="card-text">${escapeHtml(p.deskripsi || '')}</p>

                <div class="mt-3 d-flex gap-2">
                    <button class="btn btn-sm btn-outline-primary btn-edit">Edit</button>
                    <button class="btn btn-sm btn-outline-danger btn-delete">Hapus</button>
                </div>
            </div>
        `;
        card.dataset.index = index;
        card.dataset.id = p.id;
        return card;
    }

    function showAlert(type, message) {
        container.innerHTML = `
            <div class="alert alert-${type}" role="alert">${escapeHtml(message)}</div>
        `;
    }

    async function loadPengaduan() {
        container.innerHTML = '<div class="d-flex justify-content-center my-5"><div class="spinner-border" role="status"></div></div>';
        try {
            const resp = await fetch(apiUrl, {
                headers: { 'Authorization': 'Token ' + token }
            });

            if (!resp.ok) throw new Error(resp.status);
            const data = await resp.json();

            const list = Array.isArray(data) ? data : data.results;
            container.innerHTML = '';

            if (!list || list.length === 0) {
                showAlert('info', 'Belum ada data pengaduan.');
                return;
            }

            const row = document.createElement('div');
            row.className = 'row';

            list.forEach((p, i) => {
                const col = document.createElement('div');
                col.className = 'col-12 col-md-6';
                col.appendChild(renderPengaduanCard(p, i));
                row.appendChild(col);
            });

            container.appendChild(row);
            attachCardHandlers(list);

        } catch (err) {
            console.error(err);
            showAlert('danger', 'Gagal memuat data pengaduan.');
        }
    }

    const pengaduanModal = new bootstrap.Modal(document.getElementById('pengaduanModal'));
    const deleteModal = new bootstrap.Modal(document.getElementById('deleteModal'));

    function attachCardHandlers(list) {
        document.querySelectorAll('.btn-edit').forEach(btn => {
            btn.onclick = (e) => {
                const card = e.target.closest('.card');
                const data = list[card.dataset.index];

                document.getElementById('pengaduan-id').value = data.id || '';
                document.getElementById('pengaduan-judul').value = data.judul || '';
                document.getElementById('pengaduan-deskripsi').value = data.deskripsi || '';
                document.getElementById('pengaduan-status').value = data.status || '';
                document.getElementById('pengaduan-tanggal_lapor').value = data.tanggal_lapor || '';
                document.getElementById('pengaduan-pelapor').value = data.pelapor || '';

                pengaduanModal.show();
            };
        });

        document.querySelectorAll('.btn-delete').forEach(btn => {
            btn.onclick = (e) => {
                const card = e.target.closest('.card');
                document.getElementById('confirm-delete-btn').dataset.id = card.dataset.id;
                deleteModal.show();
            };
        });
    }

    // SAVE
    document.getElementById('pengaduan-save-btn').addEventListener('click', async () => {
        const id = document.getElementById('pengaduan-id').value;

        const payload = {
            judul: document.getElementById('pengaduan-judul').value.trim(),
            deskripsi: document.getElementById('pengaduan-deskripsi').value.trim(),
            status: document.getElementById('pengaduan-status').value.trim(),
            tanggal_lapor: document.getElementById('pengaduan-tanggal_lapor').value.trim(),
            pelapor: document.getElementById('pengaduan-pelapor').value.trim()
        };

        if (!payload.judul) {
            alert('Alasan pengaduan wajib diisi');
            return;
        }

        const url = id ? `${apiUrl}${id}/` : apiUrl;
        const method = id ? 'PUT' : 'POST';

        try {
            const resp = await fetch(url, {
                method,
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': 'Token ' + token
                },
                body: JSON.stringify(payload)
            });

            if (!resp.ok) {
                const data = await resp.json().catch(() => ({}));
                alert(data.detail || 'Gagal menyimpan data');
                return;
            }

            pengaduanModal.hide();
            loadPengaduan();

        } catch (err) {
            console.error(err);
            alert('Terjadi kesalahan');
        }
    });

    // DELETE
    document.getElementById('confirm-delete-btn').addEventListener('click', async (e) => {
        const id = e.target.dataset.id;
        if (!id) return;

        try {
            await fetch(`${apiUrl}${id}/`, {
                method: 'DELETE',
                headers: { 'Authorization': 'Token ' + token }
            });

            deleteModal.hide();
            loadPengaduan();
        } catch (err) {
            console.error(err);
            alert('Gagal menghapus');
        }
    });

    // ADD
    document.getElementById('add-pengaduan-btn').addEventListener('click', () => {
        document.getElementById('pengaduan-form').reset();
        document.getElementById('pengaduan-id').value = '';
        pengaduanModal.show();
    });

    loadPengaduan();
});
