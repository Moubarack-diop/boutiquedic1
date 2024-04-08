function afficherEtapeDeux() {
    document.getElementById("form-inscription").style.display = "none";
    document.getElementById("form-etape-2").style.display = "block";
}

function afficherEtapeUn() {
    document.getElementById("form-etape-2").style.display = "none";
    document.getElementById("form-inscription").style.display = "block";
}

function afficherConnexion() {
    document.getElementById("form-connexion").style.display = "block";
    document.getElementById("form-inscription").style.display = "none";
    document.getElementById("form-etape-2").style.display="none"
    document.getElementById("btnConnexion").classList.add("active");
    document.getElementById("btnInscription").classList.remove("active");
}

function afficherInscription() {
    document.getElementById("form-inscription").style.display = "block";
    document.getElementById("form-connexion").style.display = "none";
    document.getElementById("btnInscription").classList.add("active");
    document.getElementById("btnConnexion").classList.remove("active");
}
