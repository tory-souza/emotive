document.addEventListener("DOMContentLoaded", function () {
    const pontos = document.querySelectorAll('.ponto');
    const informacaoDiv = document.getElementById('informacao');
    let selectedArea = ''; // Variável para armazenar a área selecionada

    // Adiciona evento de clique para os pontos na imagem
    pontos.forEach(ponto => {
        ponto.addEventListener('click', () => {
            // Obtém a área do atributo data-area
            selectedArea = ponto.getAttribute('data-area');
            informacaoDiv.innerHTML = `Você clicou na área: <strong>${selectedArea}</strong>.`;
        });
    });

    // Função para enviar os dados do formulário
    window.sendMood = function(intensity) {
        // Verifica se uma área foi selecionada
        if (!selectedArea) {
            alert("Por favor, selecione uma área do corpo clicando na imagem.");
            return;
        }

        // Verifica se a intensidade foi selecionada
        if (!intensity) {
            alert("Por favor, selecione a intensidade da dor.");
            return;
        }

        // Define os valores dos inputs ocultos do formulário
        document.getElementById("painLocation").value = selectedArea;
        document.getElementById("painIntensity").value = intensity;

        // Submete o formulário
        document.getElementById("painForm").submit();

        // Exibe uma mensagem e redireciona após o envio
        alert("Sua dor foi registrada.");
        window.location.href = "mensagemDia";
    };
});
