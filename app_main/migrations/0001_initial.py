# Generated by Django 4.2.1 on 2023-08-07 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellidos', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('distrito', models.CharField(blank=True, max_length=100, null=True, verbose_name='Distrito')),
                ('fecha', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('presbiteriales', models.PositiveIntegerField()),
                ('nacionales', models.PositiveIntegerField()),
                ('licenciados', models.PositiveIntegerField()),
                ('ordenados', models.PositiveIntegerField()),
                ('total_cuerpo_ministerial', models.PositiveIntegerField(blank=True, null=True)),
                ('templos_oficiales', models.PositiveIntegerField()),
                ('templos_no_oficiales', models.PositiveIntegerField()),
                ('casa_templo', models.PositiveIntegerField()),
                ('tabernaculos', models.PositiveIntegerField(verbose_name='Tabernáculos/Naves')),
                ('casas_pastorales', models.PositiveIntegerField()),
                ('iglesias', models.PositiveIntegerField()),
                ('misiones', models.PositiveIntegerField()),
                ('casas_cultos', models.PositiveIntegerField(verbose_name='Casas Cultos/Células')),
                ('ministros', models.PositiveIntegerField()),
                ('miembros', models.PositiveIntegerField()),
                ('visitantes', models.PositiveIntegerField()),
                ('ninnos', models.PositiveIntegerField()),
                ('total_afiliacion_oficial', models.PositiveIntegerField()),
                ('jovenes', models.PositiveIntegerField(verbose_name='Jóvenes')),
                ('damas', models.PositiveIntegerField()),
                ('caballeros', models.PositiveIntegerField()),
                ('promedio_asistencia', models.FloatField()),
                ('bautizados_espiritu', models.FloatField()),
                ('lideres_locales', models.PositiveIntegerField(verbose_name='Líderes locales')),
                ('obreros_tiempo_completo', models.PositiveIntegerField()),
                ('estudiantes', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Presbiterio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellidos', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('fecha', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('presbiterio', models.CharField(blank=True, max_length=500, null=True)),
                ('presbiteriales', models.PositiveIntegerField()),
                ('nacionales', models.PositiveIntegerField()),
                ('licenciados', models.PositiveIntegerField()),
                ('ordenados', models.PositiveIntegerField()),
                ('total_cuerpo_ministerial', models.PositiveIntegerField(blank=True, null=True)),
                ('templos_oficiales', models.PositiveIntegerField()),
                ('templos_no_oficiales', models.PositiveIntegerField()),
                ('casa_templo', models.PositiveIntegerField()),
                ('tabernaculos', models.PositiveIntegerField(verbose_name='Tabernáculos/Naves')),
                ('casas_pastorales', models.PositiveIntegerField()),
                ('iglesias', models.PositiveIntegerField()),
                ('misiones', models.PositiveIntegerField()),
                ('casas_cultos', models.PositiveIntegerField(verbose_name='Casas Cultos/Células')),
                ('ministros', models.PositiveIntegerField()),
                ('miembros', models.PositiveIntegerField()),
                ('visitantes', models.PositiveIntegerField()),
                ('ninnos', models.PositiveIntegerField()),
                ('total_afiliacion_oficial', models.PositiveIntegerField()),
                ('jovenes', models.PositiveIntegerField(verbose_name='Jóvenes')),
                ('damas', models.PositiveIntegerField()),
                ('caballeros', models.PositiveIntegerField()),
                ('promedio_asistencia', models.FloatField()),
                ('bautizados_espiritu', models.FloatField()),
                ('lideres_locales', models.PositiveIntegerField(verbose_name='Líderes locales')),
                ('obreros_tiempo_completo', models.PositiveIntegerField()),
                ('estudiantes', models.PositiveIntegerField()),
                ('distrito', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_main.distrito')),
            ],
        ),
    ]