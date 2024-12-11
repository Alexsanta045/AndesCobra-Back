# Generated by Django 5.0.7 on 2024-12-11 15:37

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Campañas",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("nombre", models.CharField(max_length=50)),
                ("descripcion", models.TextField(max_length=500)),
                ("fecha_creacion", models.DateTimeField(auto_now_add=True)),
                ("fecha_actualizacion", models.DateField(auto_now_add=True)),
                ("img", models.URLField(blank=True, max_length=500, null=True)),
                ("campos_opcionales", models.JSONField(blank=True, default=dict)),
            ],
        ),
        migrations.CreateModel(
            name="Clientes",
            fields=[
                (
                    "nit",
                    models.CharField(max_length=15, primary_key=True, serialize=False),
                ),
                ("nombres", models.CharField(max_length=70)),
                ("tipo_id", models.CharField(blank=True, max_length=10, null=True)),
                ("apellidos", models.CharField(blank=True, max_length=50, null=True)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("direccion", models.CharField(blank=True, max_length=80, null=True)),
                ("ciudad", models.CharField(blank=True, max_length=50, null=True)),
                ("fecha_nacimiento", models.DateField(blank=True, null=True)),
                ("fecha_ingreso", models.DateField(blank=True, null=True)),
                (
                    "actividad_economica",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("genero", models.CharField(blank=True, max_length=15, null=True)),
                ("empresa", models.CharField(blank=True, max_length=60, null=True)),
                ("cantidad_hijos", models.IntegerField(blank=True, null=True)),
                ("estrato", models.IntegerField(blank=True, null=True)),
                (
                    "calificacion_cliente",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=4, null=True
                    ),
                ),
                (
                    "tipo_persona",
                    models.CharField(blank=True, max_length=60, null=True),
                ),
                ("profesion", models.CharField(blank=True, max_length=60, null=True)),
                (
                    "estado_fraude",
                    models.CharField(blank=True, max_length=70, null=True),
                ),
                (
                    "calificacion_buro",
                    models.CharField(blank=True, max_length=60, null=True),
                ),
                ("codigo_dane", models.CharField(blank=True, max_length=10, null=True)),
                (
                    "campos_opcionales",
                    models.JSONField(blank=True, default=dict, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Codeudores",
            fields=[
                (
                    "nit",
                    models.CharField(max_length=15, primary_key=True, serialize=False),
                ),
                ("nombres", models.CharField(max_length=70)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("direccion", models.CharField(blank=True, max_length=80, null=True)),
                ("ciudad", models.CharField(blank=True, max_length=50, null=True)),
                ("codigo_dane", models.CharField(blank=True, max_length=10, null=True)),
                (
                    "campos_opcionales",
                    models.JSONField(blank=True, default=dict, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PasswordChangeRequest",
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
                ("email_or_username", models.CharField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("is_changed", models.BooleanField(default=False)),
                ("changed_at", models.DateTimeField(blank=True, null=True)),
                ("is_rejected", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="PasswordChangeRequest",
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
                ("email_or_username", models.CharField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("is_changed", models.BooleanField(default=False)),
                ("changed_at", models.DateTimeField(blank=True, null=True)),
                ("is_rejected", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Referencias",
            fields=[
                (
                    "nit",
                    models.CharField(max_length=15, primary_key=True, serialize=False),
                ),
                ("nombres", models.CharField(max_length=40)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("direccion", models.CharField(blank=True, max_length=80, null=True)),
                ("ciudad", models.CharField(blank=True, max_length=50, null=True)),
                ("codigo_dane", models.CharField(blank=True, max_length=10, null=True)),
                (
                    "campos_opcionales",
                    models.JSONField(blank=True, default=dict, null=True),
                ),
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
            options={
                "db_table": "roles",
            },
        ),
        migrations.CreateModel(
            name="Tipo_gestion",
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
            ],
        ),
        migrations.CreateModel(
            name="CustomUser",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("estado", models.BooleanField(default=False)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
                (
                    "role",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="crm_api.roles",
                    ),
                ),
            ],
            options={
                "db_table": "custom_user",
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
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
                ("fecha_asignacion", models.DateField(auto_now_add=True)),
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
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Chat",
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
                ("mensaje", models.TextField(max_length=500)),
                ("fecha", models.DateTimeField(auto_now_add=True)),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Obligaciones",
            fields=[
                (
                    "codigo",
                    models.CharField(
                        editable=False,
                        max_length=25,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("codigo_obligacion", models.IntegerField(blank=True, null=True)),
                ("valor_vencido", models.DecimalField(decimal_places=2, max_digits=11)),
                ("fecha_obligacion", models.DateField(blank=True, null=True)),
                ("fecha_vencimiento", models.DateField(blank=True, null=True)),
                (
                    "valor_obligacion",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=11, null=True
                    ),
                ),
                (
                    "valor_cuota",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "saldo_capital",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=11, null=True
                    ),
                ),
                (
                    "saldo_total",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=11, null=True
                    ),
                ),
                (
                    "tipo_producto",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("dias_mora", models.IntegerField(blank=True, null=True)),
                (
                    "valor_ultimo_pago",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=11, null=True
                    ),
                ),
                (
                    "intereses_corriente",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "intereses_mora",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                ("plazo", models.DateField(blank=True, null=True)),
                (
                    "calificacion_obligacion",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("ciclo", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "etapa_actual_obligacion",
                    models.CharField(blank=True, max_length=60, null=True),
                ),
                ("fecha_inactivacion", models.DateField(blank=True, null=True)),
                (
                    "estado_operacional",
                    models.CharField(blank=True, max_length=60, null=True),
                ),
                ("dias_mora_inicial", models.IntegerField(blank=True, null=True)),
                (
                    "rango_mora_inicial",
                    models.CharField(blank=True, max_length=70, null=True),
                ),
                (
                    "rango_mora_actual",
                    models.CharField(blank=True, max_length=70, null=True),
                ),
                ("fecha_inicio_mora", models.DateField(blank=True, null=True)),
                (
                    "tasa_interes",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=3, null=True
                    ),
                ),
                (
                    "porc_gastos_cobranza",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=3, null=True
                    ),
                ),
                (
                    "valor_gastos_cobranza",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=9, null=True
                    ),
                ),
                (
                    "valor_iva_gastos",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=7, null=True
                    ),
                ),
                (
                    "valor_otros_conceptos",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=7, null=True
                    ),
                ),
                ("fecha_castigo", models.DateField(blank=True, null=True)),
                ("cuotas_vencidas", models.IntegerField(blank=True, null=True)),
                ("cuotas_pendientes", models.IntegerField(blank=True, null=True)),
                ("cuotas_pagadas", models.IntegerField(blank=True, null=True)),
                ("libranza", models.CharField(blank=True, max_length=70, null=True)),
                ("nit_empresa", models.CharField(blank=True, max_length=15, null=True)),
                ("sucursal", models.CharField(blank=True, max_length=70, null=True)),
                ("regional", models.CharField(blank=True, max_length=70, null=True)),
                (
                    "puntaje_credito",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=3, null=True
                    ),
                ),
                (
                    "puntaje_comportamiento",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=3, null=True
                    ),
                ),
                (
                    "marca_especial",
                    models.CharField(blank=True, max_length=65, null=True),
                ),
                ("fecha_corte_obligacion", models.DateField(blank=True, null=True)),
                (
                    "fecha_facturacion_obligacion",
                    models.DateField(blank=True, null=True),
                ),
                ("campos_opcionales", models.JSONField(blank=True, default=dict)),
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
                (
                    "codeudor",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="obligaciones",
                        to="crm_api.codeudores",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Acuerdo_pago",
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
                ("valor_cuota", models.FloatField()),
                ("fecha_pago", models.DateField()),
                ("estado", models.CharField(default="Vigente")),
                (
                    "descripcion",
                    models.CharField(default="sin descripcion", max_length=60),
                ),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "codigo_obligacion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="crm_api.obligaciones",
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
                ("plan_pago_id", models.IntegerField(blank=True, null=True)),
                ("campos_opcionales", models.JSONField(blank=True, default=dict)),
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
                ("descripcion", models.TextField(blank=True, max_length=200)),
                ("efectividad", models.BooleanField(blank=True, default=False)),
                ("estado", models.BooleanField(default=False)),
                (
                    "campaña",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="crm_api.campañas",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Telefono_cliente",
            fields=[
                (
                    "numero",
                    models.CharField(max_length=15, primary_key=True, serialize=False),
                ),
                ("rating", models.IntegerField(default=0)),
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
            name="Telefono_codeudor",
            fields=[
                (
                    "numero",
                    models.CharField(max_length=15, primary_key=True, serialize=False),
                ),
                ("rating", models.IntegerField(default=0)),
                (
                    "codeudor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="crm_api.codeudores",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Telefono_referencia",
            fields=[
                (
                    "numero",
                    models.CharField(max_length=15, primary_key=True, serialize=False),
                ),
                ("rating", models.IntegerField(default=0)),
                (
                    "referencia",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="crm_api.referencias",
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
                ("fecha", models.DateTimeField(auto_now_add=True)),
                (
                    "comentarios",
                    models.TextField(blank=True, max_length=200, null=True),
                ),
                (
                    "cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="crm_api.clientes",
                    ),
                ),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
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
                    "tipo_gestion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="crm_api.tipo_gestion",
                    ),
                ),
            ],
        ),
    ]
