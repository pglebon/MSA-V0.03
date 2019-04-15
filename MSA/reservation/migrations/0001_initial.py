# Generated by Django 2.1.7 on 2019-03-07 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehicule', '0001_initial'),
        ('partenaire', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debut', models.DateTimeField()),
                ('Fin', models.DateTimeField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('create_by', models.CharField(blank=True, max_length=20, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Client', to='partenaire.Partenaire')),
                ('conducteur1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conducteur1', to='partenaire.Partenaire')),
                ('conducteur2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='conducteur2', to='partenaire.Partenaire')),
                ('vehicule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Vehicule', to='vehicule.Vehicule')),
            ],
        ),
    ]