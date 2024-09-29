document.addEventListener("DOMContentLoaded", function() {
    var popup = document.getElementById('popup');

    // Acessa o valor do atributo data-success
    var success = document.getElementById('success-data').getAttribute('data-success') === 'true';

    if (success) {
        // Mostra o popup gradualmente
        popup.style.opacity = '1';


        setTimeout(function() {
            popup.style.opacity = '0';
        }, 2000);  // 2 segundos de visibilidade
    }
});
