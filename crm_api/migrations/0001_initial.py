# Generated by Django 5.1.1 on 2024-09-20 13:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Campañas",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=50)),
                ("descripcion", models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name="Clientes",
            fields=[
                (
                    "nit",
                    models.CharField(max_length=15, primary_key=True, serialize=False),
                ),
                ("telefono", models.CharField(max_length=10)),
                ("nombres", models.CharField(max_length=40)),
                ("apellidos", models.CharField(max_length=30)),
                ("email", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Referencias",
            fields=[
                (
                    "nit",
                    models.CharField(max_length=15, primary_key=True, serialize=False),
                ),
                ("nombre", models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name="ResultadosGestion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=60)),
                ("descripcion", models.TextField(max_length=200)),
                ("efectividad", models.BooleanField(default=False)),
                ("estado", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Roles",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name="Codeudores",
            fields=[
                (
                    "nit",
                    models.CharField(max_length=15, primary_key=True, serialize=False),
                ),
                ("nombre", models.CharField(max_length=30)),
                (
                    "cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="crm_api.clientes",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Obligaciones",
            fields=[
                (
                    "codigo",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                (
                    "campaña",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="crm_api.campañas",
                    ),
                ),
                (
                    "cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="crm_api.clientes",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Pagos",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("valor", models.IntegerField(default=0)),
                ("fecha", models.DateField()),
                (
                    "cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="crm_api.clientes",
                    ),
                ),
                (
                    "obligacion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="crm_api.obligaciones",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ClientesReferencias",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "cliente_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="crm_api.clientes",
                    ),
                ),
                (
                    "referencia_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="crm_api.referencias",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Usuarios",
            fields=[
                (
                    "nit",
                    models.CharField(max_length=15, primary_key=True, serialize=False),
                ),
                ("nombres", models.CharField(max_length=40)),
                ("apellidos", models.CharField(max_length=30)),
                ("email", models.CharField(max_length=50)),
                ("telefono", models.CharField(max_length=10)),
                ("direccion", models.TextField(max_length=150)),
                (
                    "rol",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="crm_api.roles"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Gestiones",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fecha", models.DateTimeField()),
                ("comentarios", models.TextField(max_length=200)),
                (
                    "cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="crm_api.clientes",
                    ),
                ),
                (
                    "resultado",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="crm_api.resultadosgestion",
                    ),
                ),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="crm_api.usuarios",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CampañasUsuarios",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fecha_asignacion", models.DateField()),
                (
                    "campañas_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="crm_api.campañas",
                    ),
                ),
                (
                    "usuarios_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="crm_api.usuarios",
                    ),
                ),
            ],
        ),
    ]
