from django.conf import settings
from django.db import models
from django.utils import timezone

# compta matieres

class Matiere(models.Model):
     reference = models.IntegerField()
     designation_matiere = models.CharField(max_length=200)  
    

class Commande(models.Model):
     num_bon = models.IntegerField()
     reference_matiere =  models.ForeignKey(Matiere, on_delete=models.CASCADE)
     quantite = models.IntegerField()
     date_livraison = models.DateTimeField(default=timezone.now)
     prix_unitaire = models.DecimalField(max_digits=9,decimal_places=2)
     prix_total = models.DecimalField(max_digits=9,decimal_places=2)


class Magasin(models.Model):
     num_bon_commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
     emplacement = models.CharField(max_length=200)
     stock_dispo = models.IntegerField(default=0)
     stock_existant = models.IntegerField(default=0)
     

    
     def stock_dispo(self):
        self.stock = stock_dispo + Commande.quantite
        return self.stock

     def stock_existant(self):
        self.stock = Magasin.stock_dispo - Journal.qte_sorties
        return self.stock




class Journal (models.Model):
     id_journal = models.PositiveIntegerField()
     date_sorties = models.DateTimeField(default=timezone.now)
     description = models.CharField(max_length = 500)
     qte_sorties = models.PositiveIntegerField()
     reference_matiere =  models.ForeignKey(Matiere, on_delete=models.CASCADE)