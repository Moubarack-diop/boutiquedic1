# Generated by Django 4.2 on 2024-04-10 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Products", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProduitImagesModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        default="produit.png", upload_to="produit-images"
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "produit",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="images",
                        to="Products.produitmodel",
                    ),
                ),
            ],
            options={"verbose_name_plural": "Images produit",},
        ),
    ]
