from django.urls import path
from . import views
urlpatterns = [
    path('patients/', views.index),
    path('addPatient/', views.addPatient),
    path('updatePatient/<int:id>',views.updatePatient),
    path('patient/create', views.create),
    path('patient/delete/<int:id>', views.delete),
    path('patient/update',views.update),
    path('patient/details/<int:id>',views.details),
    path('rechercheParId/',views.recherche),

    path('consultation/',views.consulter),
    path('addConsultation',views.addConsultation),
    path('consultation/details/<int:id>', views.detailsConsultation),
    path('consultation/create', views.createConsultation),
    path('updateConsultation/<int:id>',views.updateConsultationUrl),
    path('consultation/delete/<int:id>', views.deleteConsultation),
    path('consultation/update', views.updateConsultation),
    path('rechercheParIdConsultation/',views.rechercheConsultation),

    path('medecin/',views.medecin),
    path('addmedecin',views.addmedecin),
    path('medecin/details/<int:id>', views.detailsmedecin),
    path('medecin/create', views.createmedecin),
    path('updatemedecin/<int:id>',views.updatemedecinUrl),
    path('medecin/delete/<int:id>', views.deletemedecin),
    path('medecin/update', views.updatemedecin),
    path('rechercheParIdmedecin/',views.recherchemedecin),

    path('rendezvous/',views.rendezvous),
    path('addrendezvous',views.addrendezvous),
    path('rendezvous/details/<int:id>', views.detailsrendezvous),
    path('rendezvous/create', views.createrendezvous),
    path('updaterendezvous/<int:id>',views.updaterendezvousUrl),
    path('rendezvous/delete/<int:id>', views.deleterendezvous),
    path('rendezvous/update', views.updaterendezvous),
    path('rechercheParIdrendezvous/',views.rechercherendezvous),
]