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
]