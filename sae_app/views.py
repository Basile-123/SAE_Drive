from django.shortcuts import render, get_object_or_404, redirect
from .models import Produit, Categorie, Client, LigneCommande

# ───── PRODUITS ─────
def produit_liste(request):
    produits = Produit.objects.all()
    return render(request, 'produits/liste.html', {'produits': produits})

def produit_ajouter(request):
    categories = Categorie.objects.all()
    if request.method == 'POST':
        Produit.objects.create(
            nom=request.POST['nom'],
            date_peremption=request.POST['date_peremption'] or None,
            marque=request.POST['marque'],
            prix=request.POST['prix'],
            categorie_id=request.POST['categorie']
        )
        return redirect('produit_liste')
    return render(request, 'produits/form.html', {'categories': categories})

def produit_modifier(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    categories = Categorie.objects.all()
    if request.method == 'POST':
        produit.nom = request.POST['nom']
        produit.date_peremption = request.POST['date_peremption'] or None
        produit.marque = request.POST['marque']
        produit.prix = request.POST['prix']
        produit.categorie_id = request.POST['categorie']
        produit.save()
        return redirect('produit_liste')
    return render(request, 'produits/form.html', {'produit': produit, 'categories': categories})

def produit_supprimer(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    produit.delete()
    return redirect('produit_liste')

# ───── CLIENTS ─────
def client_liste(request):
    clients = Client.objects.all()
    return render(request, 'clients/liste.html', {'clients': clients})

def client_ajouter(request):
    if request.method == 'POST':
        Client.objects.create(
            nom=request.POST['nom'],
            prenom=request.POST['prenom'],
            adresse=request.POST['adresse']
        )
        return redirect('client_liste')
    return render(request, 'clients/form.html')

def client_modifier(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.nom = request.POST['nom']
        client.prenom = request.POST['prenom']
        client.adresse = request.POST['adresse']
        client.save()
        return redirect('client_liste')
    return render(request, 'clients/form.html', {'client': client})

def client_supprimer(request, pk):
    client = get_object_or_404(Client, pk=pk)
    client.delete()
    return redirect('client_liste')

# ───── CATEGORIES ─────
def categorie_liste(request):
    categories = Categorie.objects.all()
    return render(request, 'categories/liste.html', {'categories': categories})


def categorie_ajouter(request):
    if request.method == 'POST':
        Categorie.objects.create(
            nom=request.POST['nom'],
            descriptif=request.POST['descriptif']
        )
        return redirect('categorie_liste')

    return render(request, 'categories/form.html')


def categorie_modifier(request, pk):
    categorie = get_object_or_404(Categorie, pk=pk)

    if request.method == 'POST':
        categorie.nom = request.POST['nom']
        categorie.descriptif = request.POST['descriptif']
        categorie.save()
        return redirect('categorie_liste')

    return render(request, 'categories/form.html', {'categorie': categorie})


def categorie_supprimer(request, pk):
    categorie = get_object_or_404(Categorie, pk=pk)
    categorie.delete()
    return redirect('categorie_liste')



import csv
import io

def import_produits(request):
    if request.method == 'POST' and request.FILES.get('fichier'):
        fichier = request.FILES['fichier']
        stream = io.StringIO(fichier.read().decode('utf-8'))
        reader = csv.DictReader(stream)
        erreurs = []
        count = 0
        for row in reader:
            try:
                cat = Categorie.objects.get(id=row['categorie_id'])
                Produit.objects.create(
                    nom=row['nom'],
                    date_peremption=row['date_peremption'] or None,
                    marque=row['marque'],
                    prix=row['prix'],
                    categorie=cat
                )
                count += 1
            except Exception as e:
                erreurs.append(f"Ligne ignorée : {row} — {e}")
        return render(request, 'produits/import.html', {'count': count, 'erreurs': erreurs, 'done': True})
    return render(request, 'produits/import.html')