from django.contrib import admin
from .models import CategorieModel, ProduitModel,  ProduitImagesModel
# Register your models here.
admin.site.register([CategorieModel, ProduitModel, ProduitImagesModel])