
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
                ("fecha_creacion", models.DateTimeField(auto_now_add=True)),
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
                ("descripcion", models.TextField(blank=True, max_length=200)),
                ("efectividad", models.BooleanField(blank=True, default=False)),
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
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("fecha_obligacion", models.DateField()),
                ("fecha_vencimiento_cuota", models.DateField()),
                ("valor_capital", models.FloatField()),
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
                ("campos_opcionales", models.JSONField(blank=True, default=dict)),
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
            name="Telefono_cliente",
            fields=[
                (
                    "numero",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("tipo", models.CharField(max_length=30)),
                ("tipo_celular", models.CharField(max_length=30)),
                ("indicativo", models.CharField(max_length=5)),
                ("extension", models.CharField(max_length=5)),
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
                ("tipo", models.CharField(max_length=30)),
                ("tipo_celular", models.CharField(max_length=30)),
                ("indicativo", models.CharField(max_length=5)),
                ("extension", models.CharField(max_length=5)),
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
                        to="crm_api.codeudores",
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
                ("email", models.EmailField(max_length=50)),
                ("telefono", models.CharField(max_length=10)),
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
