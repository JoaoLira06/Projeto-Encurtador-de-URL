async function shortenUrl() {
    const input = document.getElementById('urlInput');
    const url = input.value;

    if (!url) return;

    const response = await fetch('/shorten', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ original_url: url })
    });

    const data = await response.json();

    if (response.ok) {
        const resultDiv = document.getElementById('result');
        const shortUrlLink = document.getElementById('shortUrl');
        const accessCount = document.getElementById('accessCount');

        shortUrlLink.href = data.short_url;
        shortUrlLink.textContent = data.short_url;

        // Busca as estatísticas atualizadas
        const statsResponse = await fetch(`/stats/${data.short_code}`);
        const statsData = await statsResponse.json();
        accessCount.textContent = statsData.access_count;

        resultDiv.style.display = 'block';
    } else {
        alert('Erro ao encurtar URL. Tente novamente.');
    }
}

async function copyUrl() {
    const shortUrl = document.getElementById('shortUrl').textContent;
    await navigator.clipboard.writeText(shortUrl);
    alert('URL copiada!');
}

async function updateStats() {
    const shortUrlLink = document.getElementById('shortUrl');
    const shortCode = shortUrlLink.href.split('/').pop();

    // Espera um pouco para o servidor processar o acesso
    setTimeout(async () => {
        const statsResponse = await fetch(`/stats/${shortCode}`);
        const statsData = await statsResponse.json();
        document.getElementById('accessCount').textContent = statsData.access_count;
    }, 500);
}

