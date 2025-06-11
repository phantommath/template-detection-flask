window.addEventListener('DOMContentLoaded', () => {
    const socket = io();
    const statusEl = document.getElementById('status');

    socket.on('template_found', data => {
        statusEl.innerText = `Template encontrado no frame ${data.frame}`;
    });

    socket.on('template_not_found', () => {
        statusEl.innerText = 'Template não encontrado';
    });

    document.getElementById('upload-form').onsubmit = async e => {
        e.preventDefault();
        statusEl.innerText = 'Procurando...';
        const data = new FormData(e.target);
        const res = await fetch('/upload', { method: 'POST', body: data });
        if (!res.ok) {
            statusEl.innerText = 'Erro ao processar arquivos';
        }
    };
});
