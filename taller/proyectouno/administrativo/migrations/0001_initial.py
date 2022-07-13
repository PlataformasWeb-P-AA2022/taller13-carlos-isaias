# Generated by Django 4.0.5 on 2022-07-13 00:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Edificio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=150)),
                ('ciudad', models.CharField(max_length=30)),
                ('tipo', models.CharField(choices=[('recidencial', 'Edificio Recidencial'), ('comercial', 'Edificio Comercial')], max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Edificios',
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrePropietario', models.CharField(max_length=100)),
                ('costoDepartamento', models.DecimalField(decimal_places=2, max_digits=10000)),
                ('numeroCuartos', models.IntegerField()),
                ('edificio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departamentos', to='administrativo.edificio')),
            ],
            options={
                'verbose_name_plural': 'Departamentos',
            },
        ),
    ]
