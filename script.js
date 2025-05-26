document.getElementById('claimBtn').addEventListener('click', async function() {
    const userId = /* obter o ID do usuário logado */;
    const videoId = /* obter o ID do vídeo atual */;
    const watchedSeconds = /* tempo assistido em segundos */;
    const userWallet = /* obter o endereço da carteira Phantom do usuário */;
    const rewardAmount = 1000000; // exemplo: 0.001 SOL em lamports

    // Registrar visualização
    const viewResponse = await fetch('/api/view', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ user_id: userId, video_id: videoId, watched_seconds: watchedSeconds })
    });

    if (viewResponse.ok) {
        // Distribuir recompensa
        const rewardResponse = await fetch('/api/reward', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_wallet: userWallet, amount: rewardAmount })
        });

        if (rewardResponse.ok) {
            alert('Recompensa enviada com sucesso!');
        } else {
            alert('Erro ao enviar recompensa.');
        }
    } else {
        alert('Erro ao registrar visualização.');
    }
});
