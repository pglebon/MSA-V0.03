from django.contrib import admin

# Register your models here.
from .models import Marque
from .models import Categorie
from .models import Vehicule

class MarqueAdmin(admin.ModelAdmin):
    list_display = (
        'Marque',
    )

admin.site.register(Vehicule)
admin.site.register(Categorie)
admin.site.register(Marque,MarqueAdmin)