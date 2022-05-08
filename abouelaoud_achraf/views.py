# Import render module from django
from django.core.paginator import Paginator
from django.shortcuts import render, redirect


# Create index function to display the HTML file into the browser
from abouelaoud_achraf.models import Patient, Consultation, Medecin, RendezVous


def index(request):
    patients = Patient.objects.all()
    paginator = Paginator(patients, 10)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    # context= {'patients': patients}
    context = {
        'count': paginator.count,
        'page': page
    }
    return render(request, 'patients.html', context)


def recherche(request):
    id = request.POST.get("id")
    try:
        patient = Patient.objects.get(id=id)
    except Patient.DoesNotExist:
        return redirect('/patients')

    context = {'patient': patient}
    return render(request, 'recherche.html', context)


# pour afficher les détail d'un patient
def details(request, id):
    pateint = Patient.objects.get(id=id)
    context = {'patient': pateint}
    return render(request, 'details.html', context)


# pour supprimer un patient et redireger l'utilisateur vers index
def delete(request, id):
    try:
        patient = Patient.objects.get(id=id)
    except Patient.DoesNotExist:
        return redirect('/patients')
    patient.delete()
    return redirect('/patients')


# les deux views suivants pour modifier le Créer ajouter un patient
def addPatient(request):
    rendezvous=RendezVous.objects.all()
    context={'rendezvous':rendezvous}
    return render(request, "addPatient.html",context)


def updatePatient(request, id):
    patient = Patient.objects.get(id=id)
    rendezvous = RendezVous.objects.all()
    context = {
        'patient': patient,
        'rendezVous':rendezvous
    }
    return render(request, "updatePatient.html", context)


def create(request):
    nom = request.POST.get("nom", "").capitalize()
    prenom = request.POST.get("prenom", "").capitalize()
    email = request.POST.get("email", "")
    dateNaissance = request.POST.get("dateNaissance")
    id= request.POST.get("dateRendezvous")
    rendezvous = RendezVous.objects.get(id=id)
    patient = Patient.objects.create(nom=nom, prenom=prenom,email=email, dateNaissance=dateNaissance,rendezVous=rendezvous)
    patient.save()
    return redirect("/patients")


# implémentez vous les views pour la modéfication; pagination (10 éléments par page) et la recherche par id
def update(request):
    nom = request.POST.get("nom", "").capitalize()
    prenom = request.POST.get("prenom", "").capitalize()
    email = request.POST.get("email", "")
    dateNaissance = request.POST.get("dateNaissance")
    id = request.POST.get("dateRendezvous")
    rendezvous = RendezVous.objects.get(id=id)
    id = request.POST.get("id")
    patient = Patient(id=id, nom=nom, prenom=prenom,email=email, dateNaissance=dateNaissance,rendezVous=rendezvous)
    patient.save()
    return redirect("/patients")

def consulter(request):
    consulters = Consultation.objects.all()
    paginator = Paginator(consulters, 10)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    # context= {'patients': patients}
    context = {
        'count': paginator.count,
        'page': page
    }
    return render(request, 'consulter.html', context)
def addConsultation(request):
    return render(request,"addConsultation.html")
def detailsConsultation(request,id):
    consultation = Consultation.objects.get(id=id)
    context = {'consulter': consultation}
    return render(request, 'detailsConsultation.html', context)
def updateConsultationUrl(request, id):
    consulter = Consultation.objects.get(id=id)
    context = {'consultation': consulter}
    return render(request, "updateConsultation.html", context)

def createConsultation(request):
    description = request.POST.get("description", "").capitalize()
    traitement = request.POST.get("traitement", "").capitalize()
    typeDeConsultation = request.POST.get("typeDeConsultation", "")
    consulter = Consultation.objects.create(description=description, traitement=traitement, typeDeConsultation=typeDeConsultation)
    consulter.save()
    return redirect("/consultation")


def updateConsultation(request):
    description = request.POST.get("description", "").capitalize()
    traitement = request.POST.get("traitement", "").capitalize()
    typeDeConsultation = request.POST.get("typeDeConsultation", "")
    id = request.POST.get("id")
    consulter = Consultation(id=id,description=description, traitement=traitement,typeDeConsultation=typeDeConsultation)
    consulter.save()
    return redirect("/consultation")
def deleteConsultation(request,id):
    try:
        consulter= Consultation.objects.get(id=id)
    except Consultation.DoesNotExist:
        return redirect('/consultation')
    consulter.delete()
    return redirect('/consultation')
def rechercheConsultation(request):
    id = request.POST.get("id")
    try:
        consulter = Consultation.objects.get(id=id)
    except Consultation.DoesNotExist:
        return redirect('/consultation')
    context = {'consulter': consulter}
    return render(request, 'rechercheConsultation.html', context)


def medecin(request):
    medecins = Medecin.objects.all()
    paginator = Paginator(medecins, 10)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    # context= {'patients': patients}
    context = {
        'count': paginator.count,
        'page': page
    }
    return render(request, 'medecin.html', context)

def addmedecin(request):
    return render(request,"addmedecin.html")
def detailsmedecin(request,id):
    medecin = Medecin.objects.get(id=id)
    context = {'medecin': medecin}
    return render(request, 'detailsMedecin.html', context)
def updatemedecinUrl(request, id):
    consulter = Medecin.objects.get(id=id)
    context = {'medecin': consulter}
    return render(request, "updateMedecin.html", context)

def createmedecin(request):
    nom = request.POST.get("nom","").capitalize()
    prenom = request.POST.get("prenom","").capitalize()
    specialiter=request.POST.get("specialiter","")
    medecin=Medecin.objects.create(nom=nom,prenom=prenom,specialiter=specialiter)
    medecin.save()
    return redirect("/medecin")


def updatemedecin(request):
    id=request.POST.get("id")
    nom = request.POST.get("nom", "").capitalize()
    prenom = request.POST.get("prenom", "").capitalize()
    specialiter = request.POST.get("specialiter", "")
    medecin = Medecin(id=id,nom=nom, prenom=prenom, specialiter=specialiter)
    medecin.save()
    return redirect("/medecin")
def deletemedecin(request,id):
    try:
        consulter= Medecin.objects.get(id=id)
    except Medecin.DoesNotExist:
        return redirect('/medecin')
    consulter.delete()
    return redirect('/medecin')
def recherchemedecin(request):
    id = request.POST.get("id")
    try:
        medecin = Medecin.objects.get(id=id)
    except Medecin.DoesNotExist:
        return redirect('/medecin')
    context = {'medecin': medecin}
    return render(request, 'rechercheMedecin.html', context)

#rebdezcvous

def rendezvous(request):
    rendezvouss = RendezVous.objects.all()
    paginator = Paginator(rendezvouss, 10)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    # context= {'patients': patients}
    context = {
        'count': paginator.count,
        'page': page
    }
    return render(request, 'rendezvous.html', context)

def addrendezvous(request):
    medecin = Medecin.objects.all()
    consulter = Consultation.objects.all()
    context = {
        'medecins':medecin,
        'consulters':consulter
    }
    return render(request,"addrendezvous.html",context)
def detailsrendezvous(request,id):
    rendezvous = RendezVous.objects.get(id=id)
    context = {'rendezvous': rendezvous}
    return render(request, 'detailsrendezvous.html', context)
def updaterendezvousUrl(request, id):
    rendezvous = RendezVous.objects.get(id=id)
    medecin = Medecin.objects.all()
    consulter = Consultation.objects.all()
    context = {
        'medecins': medecin,
        'consulters': consulter,
        'rendezvous':rendezvous
    }
    return render(request, "updaterendezvous.html", context)

def createrendezvous(request):
    try:
        dateRendezVous=request.POST.get("dateRendezVous","")
        isCanceled=request.POST.get("isCanceled")
        idMedecin = request.POST.get("medecin")
        idConsulter = request.POST.get("consulter")
        medecin = Medecin.objects.get(id=idMedecin)
        consulter = Consultation.objects.get(id=idConsulter)
        rendezvous=RendezVous.objects.create(isCanceled=isCanceled,dateRendezVous=dateRendezVous,medecin=medecin,consultation=consulter)
        rendezvous.save()
    except Exception:
        return redirect("/rendezvous")
    return redirect("/rendezvous")


def updaterendezvous(request):
    try:
        id=request.POST.get("id")
        dateRendezVous = request.POST.get("dateRendezVous", "")
        isCanceled = request.POST.get("iscanceled","")
        idMedecin = request.POST.get("medecin")
        idConsulter = request.POST.get("consulter")
        medecin = Medecin.objects.get(id=idMedecin)
        consulter = Consultation.objects.get(id=idConsulter)
        rendezvous = RendezVous(id=id,isCanceled=isCanceled,dateRendezVous=dateRendezVous,medecin=medecin,consultation=consulter)
        rendezvous.save()
    except Exception:
        return redirect("/rendezvous")
    return redirect("/rendezvous")
def deleterendezvous(request,id):
    try:
        consulter=RendezVous.objects.get(id=id)
    except RendezVous.DoesNotExist:
        return redirect('/rendezvous')
    consulter.delete()
    return redirect('/rendezvous')
def rechercherendezvous(request):
    try:
        id = request.POST.get("id")
        rendezvous = RendezVous.objects.get(id=id)
    except RendezVous.DoesNotExist:
        return redirect("/rendezvous")
    context = {'rendezvous': rendezvous}
    return render(request, 'rechercherendezvous.html', context)