document.addEventListener("DOMContentLoaded", function() {
    // Função para abrir o modal
    function openModal(modalId) {
        // Garantir que o modal com o id seja mostrado
        document.getElementById(modalId).style.display = 'flex'; // Exibe o modal
    }

    // Função para fechar o modal
    function closeModal(modalId) {
        // Esconde o modal
        document.getElementById(modalId).style.display = 'none';
    }

    // Adicionando eventos de clique para abrir modais
    document.getElementById("openModalBtn1").onclick = function() { openModal('loginModal1'); };
    document.getElementById("openModal2Btn").onclick = function() { openModal('loginModal2'); };
    document.getElementById("openModalBtn3").onclick = function() { openModal('loginModal3'); };
    document.getElementById("openModal4Btn").onclick = function() { openModal('loginModal4'); };

    // Adicionando eventos de clique para fechar modais
    document.getElementById("closeModalBtn1").onclick = function() { closeModal('loginModal1'); };
    document.getElementById("closeModalBtn2").onclick = function() { closeModal('loginModal2'); };
    document.getElementById("closeModalBtn3").onclick = function() { closeModal('loginModal3'); };
    document.getElementById("closeModalBtn4").onclick = function() { closeModal('loginModal4'); };

    // Fechar os modais ao clicar fora deles
    window.onclick = function(event) {
        if (event.target.classList.contains("modal")) {
            event.target.style.display = "none";
        }
    };
});
