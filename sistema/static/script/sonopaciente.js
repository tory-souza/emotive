// Função para selecionar o humor
function selectMood(button, mood) {
    // Remover a classe "selected" de todos os botões
    const buttons = document.querySelectorAll('.mood-buttons button');
    buttons.forEach(function(btn) {
        btn.classList.remove('selected');
    });

    // Adicionar a classe "selected" ao botão clicado
    button.classList.add('selected');

    // Ativar o botão "Enviar"
    document.getElementById('submitButton').disabled = false;
}

// Quando o formulário for submetido, redireciona para intensidade.html
document.getElementById('moodForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Impede o envio padrão do formulário
    alert("Sua Mensagem foi Enviada com Sucesso!.");
    window.location.href = 'intensidade'; // Redireciona para a página de intensidade
});
