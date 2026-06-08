from django.shortcuts import render, get_object_or_404, redirect
from .models import Produit, Categorie, Client, Commande, LigneProduit
from .forms import CommandeForm, LigneProduitForm
from django.http import HttpResponseRedirect
import csv
import io

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

# ───── IMPORT CSV ─────
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

# ───── COMMANDES ─────
def afficher_commandes(request):
    liste = Commande.objects.all()
    return render(request, 'commandes/liste.html', {'liste': liste})

def commande_formulaire(request):
    formulaire = CommandeForm()
    return render(request, 'commandes/form.html', {'formulaire': formulaire})

def commande_traitement(request):
    formulaire = CommandeForm(request.POST)
    if formulaire.is_valid():
        formulaire.save()
        return HttpResponseRedirect('/commandes/')
    return render(request, 'commandes/form.html', {'formulaire': formulaire})

def commande_afficher_one(request, id):
    commande = Commande.objects.get(pk=id)
    lignes = commande.ligneproduit_set.all()
    return render(request, 'commandes/detail.html', {'commande': commande, 'lignes': lignes})

def commande_modifier(request, id):
    data = Commande.objects.get(pk=id)
    formulaire = CommandeForm(instance=data)
    return render(request, 'commandes/form.html', {'formulaire': formulaire, 'id': id})

def commande_sauvegarder_modif(request, id):
    data = Commande.objects.get(pk=id)
    formulaire = CommandeForm(request.POST, instance=data)
    if formulaire.is_valid():
        formulaire.save()
        return HttpResponseRedirect('/commandes/')
    return render(request, 'commandes/form.html', {'formulaire': formulaire, 'id': id})

def commande_supprimer(request, id):
    Commande.objects.get(pk=id).delete()
    return HttpResponseRedirect('/commandes/')

# ───── LIGNES ─────
def ligne_formulaire(request, id_commande):
    commande = Commande.objects.get(pk=id_commande)
    formulaire = LigneProduitForm(initial={'commande': commande})
    return render(request, 'commandes/ligne_form.html', {'formulaire': formulaire, 'commande': commande})

def ligne_traitement(request, id_commande):
    formulaire = LigneProduitForm(request.POST)
    if formulaire.is_valid():
        formulaire.save()
        return HttpResponseRedirect('/commandes/' + str(id_commande) + '/')
    commande = Commande.objects.get(pk=id_commande)
    return render(request, 'commandes/ligne_form.html', {'formulaire': formulaire, 'commande': commande})

def ligne_supprimer(request, id):
    ligne = LigneProduit.objects.get(pk=id)
    id_commande = ligne.commande_id
    ligne.delete()
    return HttpResponseRedirect('/commandes/' + str(id_commande) + '/')