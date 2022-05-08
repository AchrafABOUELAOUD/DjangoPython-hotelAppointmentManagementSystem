
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medecin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=45)),
                ('prenom', models.CharField(max_length=45)),
                ('specialier', models.CharField(max_length=45)),
            ],
        ),

        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=45)),
                ('traitement', models.CharField(max_length=45)),
                ('typeDeConsultation', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='RendezVous',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateRendezVous', models.DateField(auto_now=True)),
                ('isCanceled', models.BooleanField(default=False)),
                ('specialier', models.CharField(max_length=45)),
                ('medecin', models.ForeignKey(on_delete=django.db.models.CASCADE, related_name='medecin',to='abouelaoud_achraf.medecin')),
                ('consultation', models.OneToOneField(on_delete=django.db.models.CASCADE, related_name='consultation',to='abouelaoud_achraf.consultation'))

            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=45)),
                ('prenom', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
                ('dateNaissance', models.DateField(auto_now=True)),
                ('rendezVous',models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='RendezVous', to='abouelaoud_achraf.rendezVous'))
            ],

        ),

    ]
