from django.contrib import admin

# Register your models here.
from abouelaoud_achraf.models import Patient, Medecin, RendezVous, Consultation

admin.site.register(Patient)
admin.site.register(Medecin)
admin.site.register(RendezVous)
admin.site.register(Consultation)