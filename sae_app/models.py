from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    descriptif = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'categorie'

    def __str__(self):
        return self.nom

class Produit(models.Model):
    nom = models.CharField(max_length=150)
    date_peremption = models.DateField(blank=True, null=True)
    photo = models.CharField(max_length=255, blank=True, null=True)
    marque = models.CharField(max_length=100, blank=True, null=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'produit'

    def __str__(self):
        return self.nom

class Client(models.Model):
    numero_client = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_inscription = models.DateField(auto_now_add=True)
    adresse = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'client'

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Commande(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)

    def cout_total(self):
        total = 0
        for ligne in self.ligneproduit_set.all():
            total += ligne.sous_total()
        return total

    def __str__(self):
        return f"Commande n°{self.id} - {self.client} - {self.date}"

    class Meta:
        db_table = 'commande'

class LigneProduit(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.IntegerField(default=1)

    def sous_total(self):
        return self.produit.prix * self.quantite

    def __str__(self):
        return f"{self.quantite} x {self.produit.nom}"

    class Meta:
        db_table = 'ligne_commande'