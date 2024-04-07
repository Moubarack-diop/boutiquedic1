from django.shortcuts import render
from .forms import InscriptionForm

def view_log(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            # Traitez les données du formulaire si nécessaire
            form.save()
            # Redirigez l'utilisateur vers une page de confirmation ou autre
    else:
        form = InscriptionForm()
    return render(request, 'users/log.html', {'form': form})
