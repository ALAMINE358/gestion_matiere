from django.contrib import admin

# Register your models here.
from .models import Matiere,Commande,Magasin,Journal

admin.site.register(Matiere)
admin.site.register(Commande)
admin.site.register(Magasin)
admin.site.register(Journal)