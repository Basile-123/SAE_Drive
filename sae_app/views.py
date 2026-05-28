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