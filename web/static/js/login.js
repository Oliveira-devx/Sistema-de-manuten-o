/*
   ==========================================================================
   ARQUIVO: login.js
   FINALIDADE: Adicionar interatividades e animações dinâmicas à tela de login.
   ==========================================================================
*/

document.addEventListener('DOMContentLoaded', () => {

    const loginForm = document.querySelector('.login-form');
    const btnLogin = document.querySelector('.btn-login');

    // Novos elementos para a funcionalidade de ver senha
    const togglePassword = document.getElementById('toggle-password');
    const passwordInput = document.getElementById('senha');

    // --- Funcionalidade: Mostrar/Ocultar Senha ---

    // Escuta a mudança de estado do checkbox "Ver senha"
    togglePassword.addEventListener('change', function() {
        // Se o checkbox estiver marcado (true), muda o tipo do input para 'text' (visível)
        // Se estiver desmarcado (false), volta para 'password' (oculto)
        if (this.checked) {
            passwordInput.setAttribute('type', 'text');
        } else {
            passwordInput.setAttribute('type', 'password');
        }
    });

    // --- Efeito de Interação no Botão de Login ---

    btnLogin.addEventListener('mouseenter', () => {
        btnLogin.style.transition = 'all 0.3s ease';
        btnLogin.style.boxShadow = '0 0 15px rgba(26, 42, 108, 0.5)';
    });

    btnLogin.addEventListener('mouseleave', () => {
        btnLogin.style.boxShadow = 'none';
    });

    // --- Simulação de Processamento no Clique ---

    loginForm.addEventListener('submit', (event) => {
        event.preventDefault();

        const textoOriginal = btnLogin.innerText;
        btnLogin.innerText = 'Autenticando...';

        btnLogin.disabled = true;
        btnLogin.style.opacity = '0.7';
        btnLogin.style.cursor = 'not-allowed';

        setTimeout(() => {
            btnLogin.innerText = textoOriginal;
            btnLogin.disabled = false;
            btnLogin.style.opacity = '1';
            btnLogin.style.cursor = 'pointer';

            alert('Esta é uma demonstração visual. A integração real com o Python será feita em uma etapa futura!');
        }, 1500);
    });

    // --- Animações de Entrada dos Campos (Staggered Animation) ---

    const inputGroups = document.querySelectorAll('.input-group');

    inputGroups.forEach((group, index) => {
        group.style.opacity = '0';
        group.style.transform = 'translateY(20px)';
        group.style.transition = 'all 0.5s ease';

        setTimeout(() => {
            group.style.opacity = '1';
            group.style.transform = 'translateY(0)';
        }, 200 * (index + 1));
    });
});
