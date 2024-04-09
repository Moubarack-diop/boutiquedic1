//Losqu'on clique sur l'input de type radio un evenement(click) est declenche sur son element parent ie le lien parent 
//ce qui declenche une redirection vers l'url defini dans le lien
radioButtonElement = document.querySelectorAll('input[type="radio"]');
radioButtonElement.forEach(function(radio) {
    radio.addEventListener("click", function() {
        radio.parentElement.click();
        }
    )
});      
