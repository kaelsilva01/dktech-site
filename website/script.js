
async function verificarAPI() {
    const status = document.getElementById("api-status");
    const mensagem = document.getElementById("api-message");

    try {
        const resposta = await fetch("/api/");

        if (!resposta.ok) {
            throw new Error("Erro na comunicação com a API");
        }

        const dados = await resposta.json();

        status.textContent = "API: " + dados.status;
        mensagem.textContent = dados.mensagem;

    } catch (erro) {
        status.textContent = "API offline";
        mensagem.textContent = "Não foi possível conectar ao servidor.";
        console.error(erro);
    }
}

verificarAPI();
