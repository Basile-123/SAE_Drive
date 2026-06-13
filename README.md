# SAE Drive — Application Django

## Présentation du projet

Ce projet a été réalisé dans le cadre de la SAÉ 2.03.  
L’objectif était de développer une application web de type **Drive de supermarché** avec le framework **Django**.

L’application permet de gérer plusieurs éléments d’un drive :

- les produits ;
- les catégories ;
- les clients ;
- les commandes ;
- les lignes de commande.

Le projet repose sur une architecture simple : Django gère la partie web, les modèles représentent les tables de la base de données, les vues traitent les actions de l’utilisateur, et les templates affichent les pages HTML.

---

## Fonctionnalités principales

### Gestion des produits

L’application permet de gérer les produits du drive avec plusieurs informations :

- nom du produit ;
- date de péremption ;
- marque ;
- prix ;
- catégorie associée.

Chaque produit est relié à une catégorie grâce à une clé étrangère.

---

### Gestion des catégories

Ma partie principale du projet concerne le **CRUD des catégories**.

Un CRUD permet de réaliser quatre actions :

- **Create** : ajouter une catégorie ;
- **Read** : afficher la liste des catégories ;
- **Update** : modifier une catégorie existante ;
- **Delete** : supprimer une catégorie.

Les catégories permettent de classer les produits du drive, par exemple :

- Fruits et légumes ;
- Boissons ;
- Surgelés ;
- Hygiène ;
- Épicerie.

Cette partie m’a permis de mieux comprendre le lien entre :

- le modèle Django ;
- la vue ;
- l’URL ;
- le template HTML ;
- la base de données.

---

### Gestion des clients

L’application permet aussi de gérer les clients du drive.

Un client possède :

- un numéro client ;
- un nom ;
- un prénom ;
- une date d’inscription ;
- une adresse.

---

### Gestion des commandes

Le projet contient également une gestion des commandes.

Une commande est liée à un client.  
Une commande peut contenir plusieurs produits grâce aux lignes de commande.

Chaque ligne de commande contient :

- une commande ;
- un produit ;
- une quantité.

Cela permet de calculer le contenu d’une commande et son coût total.

---

## Structure de la base de données

Le projet contient plusieurs tables principales :

| Table | Rôle |
|---|---|
| `categorie` | Stocke les catégories de produits |
| `produit` | Stocke les produits du drive |
| `client` | Stocke les clients |
| `commande` | Stocke les commandes |
| `ligne_commande` | Fait le lien entre les commandes et les produits |

Les relations principales sont :

- un produit appartient à une catégorie ;
- une commande appartient à un client ;
- une ligne de commande relie une commande à un produit.

---

## Technologies utilisées

- Python
- Django
- HTML
- CSS
- SQLite en développement
- MariaDB prévu pour l’architecture avec deux VM
- Git / GitHub
- VirtualBox pour les machines virtuelles

---

## Architecture prévue avec les VM

Le projet peut être utilisé avec deux machines virtuelles :

```text
VM_DJANGO  → application web Django
VM_MARIA   → base de données MariaDB
