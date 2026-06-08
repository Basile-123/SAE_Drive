from django.contrib import admin
from django.urls import path
from sae_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Produits
    path('produits/', views.produit_liste, name='produit_liste'),
    path('produits/ajouter/', views.produit_ajouter, name='produit_ajouter'),
    path('produits/modifier/<int:pk>/', views.produit_modifier, name='produit_modifier'),
    path('produits/supprimer/<int:pk>/', views.produit_supprimer, name='produit_supprimer'),
    path('produits/import/', views.import_produits, name='import_produits'),

    # Clients
    path('clients/', views.client_liste, name='client_liste'),
    path('clients/ajouter/', views.client_ajouter, name='client_ajouter'),
    path('clients/modifier/<int:pk>/', views.client_modifier, name='client_modifier'),
    path('clients/supprimer/<int:pk>/', views.client_supprimer, name='client_supprimer'),

    # Catégories
    path('categories/', views.categorie_liste, name='categorie_liste'),
    path('categories/ajouter/', views.categorie_ajouter, name='categorie_ajouter'),
    path('categories/modifier/<int:pk>/', views.categorie_modifier, name='categorie_modifier'),
    path('categories/supprimer/<int:pk>/', views.categorie_supprimer, name='categorie_supprimer'),

    # Commandes
    path('commandes/', views.afficher_commandes, name='commandes'),
    path('commandes/ajouter/', views.commande_formulaire, name='commande_ajouter'),
    path('commandes/traitement/', views.commande_traitement, name='commande_traitement'),
    path('commandes/<int:id>/', views.commande_afficher_one, name='commande_detail'),
    path('commandes/modifier/<int:id>/', views.commande_modifier, name='commande_modifier'),
    path('commandes/sauvegarder/<int:id>/', views.commande_sauvegarder_modif, name='commande_sauvegarder'),
    path('commandes/supprimer/<int:id>/', views.commande_supprimer, name='commande_supprimer'),

    # Lignes
    path('commandes/<int:id_commande>/ligne/ajouter/', views.ligne_formulaire, name='ligne_ajouter'),
    path('commandes/<int:id_commande>/ligne/traitement/', views.ligne_traitement, name='ligne_traitement'),
    path('lignes/supprimer/<int:id>/', views.ligne_supprimer, name='ligne_supprimer'),
]