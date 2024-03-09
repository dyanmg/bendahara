const forms = document.querySelectorAll('.delete-form');

for (const form of forms) {
    form.addEventListener('submit', e => {
        if (confirm('Yakin menghapus entry?')) {
            return true;
        }
        e.preventDefault();
        return false;
    });
}