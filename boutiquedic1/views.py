from django.shortcuts import render, redirect
from django.contrib import messages
from Products.models import CategorieModel, ProduitModel


def view_home(request):
    produits = ProduitModel.objects.all()
    categories = CategorieModel.objects.all()
    return render(request, "accueuil.html", context={'produits': produits, 'categories': categories})

def view_category_list_products(request, name):
    name = name.replace('-', ' ')
    print(name)
    categories = CategorieModel.objects.all()
    try:
        categorie = CategorieModel.objects.get(titre=name)
        produits = ProduitModel.objects.filter(categorie=categorie) 
        
        return render(request, 'produits_par_categorie.html', {'produits':produits, 'categorie':categorie,'categories':categories })
    except:
        #messages.error(request, ("Cette categorie n'existe pas"))
        return redirect('home-path')