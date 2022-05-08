from django.db import models
from datetime import datetime, date


# Create your models here.

class Medecin(models.Model):
    nom = models.CharField(max_length=45)
    prenom = models.CharField(max_length=45)
    specialiter = models.CharField(max_length=45)


class Consultation(models.Model):
    description = models.CharField(max_length=45)
    traitement = models.CharField(max_length=45)
    typeDeConsultation = models.CharField(max_length=45)


class RendezVous(models.Model):
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE, related_name="Medecin")
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE, related_name="consultation")
    dateRendezVous = models.DateField(null=True)
    isCanceled = models.BooleanField(default=False)


class Patient(models.Model):
    nom = models.CharField(max_length=45)
    prenom = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    dateNaissance = models.DateField(null=True)
    rendezVous = models.ForeignKey(RendezVous, on_delete=models.CASCADE, related_name="rendezVous")
