from django.shortcuts import render
from Products.models import CategorieModel, ProduitModel


def view_home(request):
    produits = ProduitModel.objects.all()
    for p in produits:
        print(p.image.url)
    categories = CategorieModel.objects.all()
    return render(request, "accueuil.html", context={'produits': produits, 'categories': categories})

