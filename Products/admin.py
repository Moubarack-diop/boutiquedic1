from django.contrib import admin
from .models import CategorieModel, ProduitModel
# Register your models here.
admin.site.register([CategorieModel, ProduitModel])