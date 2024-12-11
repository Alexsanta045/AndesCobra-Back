# Generated by Django 5.0.7 on 2024-12-05 14:39

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
            name="Canales",
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
                ("telefonico", models.BooleanField(default=True)),
                ("visita", models.BooleanField(default=False)),
                ("whatsapp", models.BooleanField(default=False)),
                ("email", models.BooleanField(default=False)),
                ("sms", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Departamento",
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
            ],
        ),
        migrations.CreateModel(
            name="Pais",
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
                ("nombre", models.CharField(max_length=40)),
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
            name="Tipo_identificacion",
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
                ("nombre", models.CharField(max_length=20)),
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
            name="Clientes",
            fields=[
                (
                    "nit",
                    models.CharField(max_length=15, primary_key=True, serialize=False),
                ),
                ("nombres", models.CharField(max_length=40)),
                ("apellidos", models.CharField(max_length=30)),
                ("email", models.CharField(max_length=50)),
                ("campos_opcionales", models.JSONField(blank=True, default=dict)),
                (
                    "canales_autorizados",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="crm_api.canales",
                    ),
                ),
                (
                    "tipo_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="crm_api.tipo_identificacion",
                    ),
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
            name="Ciudad",
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
                (
                    "departamento",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="crm_api.departamento",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Direccion_cliente",
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
                ("barrio", models.CharField(max_length=50)),
                ("vereda", models.CharField(blank=True, max_length=20)),
                ("calle", models.CharField(blank=True, max_length=15)),
                ("carrera", models.CharField(blank=True, max_length=10)),
                ("complemento", models.CharField(blank=True, max_length=70)),
                (
                    "ciudad",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="crm_api.ciudad"
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
            name="Direccion_codeudor",
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
                ("barrio", models.CharField(max_length=50)),
                ("vereda", models.CharField(blank=True, max_length=20)),
                ("calle", models.CharField(blank=True, max_length=15)),
                ("carrera", models.CharField(blank=True, max_length=10)),
                ("complemento", models.CharField(blank=True, max_length=70)),
                (
                    "ciudad",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="crm_api.ciudad"
                    ),
                ),
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
                ("fecha_obligacion", models.DateField()),
                ("fecha_vencimiento_cuota", models.DateField()),
                ("valor_capital", models.FloatField(blank=True, null=True)),
                ("valor_mora", models.FloatField()),
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
        migrations.AddField(
            model_name="departamento",
            name="pais",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="crm_api.pais"
            ),
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
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("tipo", models.CharField(blank=True, max_length=30)),
                ("tipo_celular", models.CharField(blank=True, max_length=30)),
                ("indicativo", models.CharField(blank=True, max_length=5)),
                ("extension", models.CharField(blank=True, max_length=5)),
                ("rating", models.IntegerField(default=0)),
                (
                    "ciudad",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="crm_api.ciudad"
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
            name="Telefono_codeudor",
            fields=[
                (
                    "numero",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("tipo", models.CharField(blank=True, max_length=30)),
                ("tipo_celular", models.CharField(blank=True, max_length=30)),
                ("indicativo", models.CharField(blank=True, max_length=5)),
                ("extension", models.CharField(blank=True, max_length=5)),
                ("rating", models.IntegerField(default=0)),
                (
                    "ciudad",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="crm_api.ciudad"
                    ),
                ),
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
