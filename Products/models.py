from django.db import models


""" def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)  """


# Create your models here.
class CategorieModel(models.Model):
    titre = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self) -> str:
        return self.titre
    

class ProduitModel(models.Model):
    titre = models.CharField(max_length=255, default="produit")
    description = models.TextField(null=True, blank=True, default="C'est le produit")
    categorie = models.ForeignKey(CategorieModel, on_delete=models.SET_NULL, null=True, default="categorie")
    prix = models.DecimalField(max_digits=10, decimal_places=2, default="0.99")
    image = models.ImageField(upload_to="produits/", default='produit.png')
    date_creation = models.DateTimeField(auto_now_add=True)
    mise_a_jour = models.DateTimeField(auto_now=True)
    en_stock = models.BooleanField(default=True)
    #en_stock? definir les autres champs restants
    #Stocker la 1ere bd obtenue
    class Meta:
        verbose_name_plural = "Produits"
    
    def __str__(self) -> str:
        return self.titre
    

class ProduitImagesModel(models.Model):
    image = models.ImageField(upload_to='produit-images', default="produit.png")
    produit = models.ForeignKey(ProduitModel, on_delete=models.SET_NULL, null=True, related_name="images")
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Images produit"
    
    def __str__(self) -> str:
        return self.produit.titre