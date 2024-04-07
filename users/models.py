from django.db import models

class UserModel(models.Model):
    prenom = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    date_naissance = models.DateField()
    email = models.EmailField(max_length=254)
    mot_de_pass = models.CharField(max_length=50)
    confirmer_mot_de_pass = models.CharField(max_length=50)


    def __str__(self):
        return self.prenom
