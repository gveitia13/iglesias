# Generated by Django 4.2.4 on 2023-09-19 07:10

import django.core.validators
from django.db import migrations, models


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
                ('fecha', models.DateField(auto_now_add=True, help_text='Se autosignará la fecha cuando sea creado', verbose_name='Fecha de creación')),
                ('cant_presbiterios', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Cantidad de presbiterios')),
                ('presbiteriales', models.PositiveIntegerField(default=0)),
                ('nacionales', models.PositiveIntegerField(default=0)),
                ('licenciados', models.PositiveIntegerField(default=0)),
                ('ordenados', models.PositiveIntegerField(default=0)),
                ('total_cuerpo_ministerial', models.PositiveIntegerField(blank=True, null=True)),
                ('templos_oficiales', models.PositiveIntegerField(default=0)),
                ('templos_no_oficiales', models.PositiveIntegerField(default=0)),
                ('casa_templo', models.PositiveIntegerField(default=0)),
                ('tabernaculos', models.PositiveIntegerField(default=0, verbose_name='Tabernáculos/Naves')),
                ('casas_pastorales', models.PositiveIntegerField(default=0)),
                ('iglesias', models.PositiveIntegerField(default=0)),
                ('misiones', models.PositiveIntegerField(default=0)),
                ('casas_cultos', models.PositiveIntegerField(default=0, verbose_name='Casas Cultos/Células')),
                ('ministros', models.PositiveIntegerField(default=0)),
                ('miembros', models.PositiveIntegerField(default=0)),
                ('visitantes', models.PositiveIntegerField(default=0)),
                ('ninnos', models.PositiveIntegerField(default=0, verbose_name='Niños')),
                ('total_afiliacion_oficial', models.PositiveIntegerField(default=0, verbose_name='Total afiliación oficial')),
                ('jovenes', models.PositiveIntegerField(default=0, verbose_name='Jóvenes')),
                ('damas', models.PositiveIntegerField(default=0)),
                ('caballeros', models.PositiveIntegerField(default=0)),
                ('total_departamento', models.PositiveIntegerField(default=0, help_text='Incluye niños', verbose_name='Total Departamento / Ministerios')),
                ('promedio_asistencia', models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0, 'Debe ser mayor o igual a cero')])),
                ('bautizados_espiritu', models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0, 'Debe ser mayor o igual a cero')], verbose_name='Bautizados Espíritu')),
                ('lideres_locales', models.PositiveIntegerField(default=0, verbose_name='Líderes locales')),
                ('obreros_tiempo_completo', models.PositiveIntegerField(default=0)),
                ('estudiantes', models.PositiveIntegerField(default=0)),
                ('evaluado', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('distrito',),
            },
        ),
        migrations.CreateModel(
            name='Presbiterio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellidos', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('fecha', models.DateField(auto_now_add=True, help_text='Se autosignará la fecha cuando sea creado', verbose_name='Fecha de creación')),
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
                ('ninnos', models.PositiveIntegerField(verbose_name='Niños')),
                ('total_afiliacion_oficial', models.PositiveIntegerField(verbose_name='Total afiliación oficial')),
                ('jovenes', models.PositiveIntegerField(verbose_name='Jóvenes')),
                ('damas', models.PositiveIntegerField()),
                ('caballeros', models.PositiveIntegerField()),
                ('total_departamento', models.PositiveIntegerField(help_text='Incluye niños', verbose_name='Total Departamento / Ministerios')),
                ('promedio_asistencia', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0, 'Debe ser mayor o igual a cero')])),
                ('bautizados_espiritu', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0, 'Debe ser mayor o igual a cero')], verbose_name='Bautizados Espíritu')),
                ('lideres_locales', models.PositiveIntegerField(verbose_name='Líderes locales')),
                ('obreros_tiempo_completo', models.PositiveIntegerField()),
                ('estudiantes', models.PositiveIntegerField()),
                ('evaluado', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('user',),
            },
        ),
        migrations.CreateModel(
            name='ResumenDistrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellidos', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('distrito', models.CharField(blank=True, max_length=100, null=True, verbose_name='Distrito')),
                ('fecha', models.DateField(verbose_name='Fecha del Distrito')),
                ('fecha_resumen', models.DateField(auto_now_add=True, verbose_name='Fecha del Resumen')),
                ('cant_presbiterios', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Cantidad de presbiterios')),
                ('presbiteriales', models.PositiveIntegerField(default=0)),
                ('nacionales', models.PositiveIntegerField(default=0)),
                ('licenciados', models.PositiveIntegerField(default=0)),
                ('ordenados', models.PositiveIntegerField(default=0)),
                ('total_cuerpo_ministerial', models.PositiveIntegerField(blank=True, null=True)),
                ('templos_oficiales', models.PositiveIntegerField(default=0)),
                ('templos_no_oficiales', models.PositiveIntegerField(default=0)),
                ('casa_templo', models.PositiveIntegerField(default=0)),
                ('tabernaculos', models.PositiveIntegerField(default=0, verbose_name='Tabernáculos/Naves')),
                ('casas_pastorales', models.PositiveIntegerField(default=0)),
                ('iglesias', models.PositiveIntegerField(default=0)),
                ('misiones', models.PositiveIntegerField(default=0)),
                ('casas_cultos', models.PositiveIntegerField(default=0, verbose_name='Casas Cultos/Células')),
                ('ministros', models.PositiveIntegerField(default=0)),
                ('miembros', models.PositiveIntegerField(default=0)),
                ('visitantes', models.PositiveIntegerField(default=0)),
                ('ninnos', models.PositiveIntegerField(default=0, verbose_name='Niños')),
                ('total_afiliacion_oficial', models.PositiveIntegerField(default=0, verbose_name='Total afiliación oficial')),
                ('jovenes', models.PositiveIntegerField(default=0, verbose_name='Jóvenes')),
                ('damas', models.PositiveIntegerField(default=0)),
                ('caballeros', models.PositiveIntegerField(default=0)),
                ('total_departamento', models.PositiveIntegerField(default=0, help_text='Incluye niños', verbose_name='Total Departamento / Ministerios')),
                ('promedio_asistencia', models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0, 'Debe ser mayor o igual a cero')])),
                ('bautizados_espiritu', models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0, 'Debe ser mayor o igual a cero')], verbose_name='Bautizados Espíritu')),
                ('lideres_locales', models.PositiveIntegerField(default=0, verbose_name='Líderes locales')),
                ('obreros_tiempo_completo', models.PositiveIntegerField(default=0)),
                ('estudiantes', models.PositiveIntegerField(default=0)),
                ('cantidad_meses', models.PositiveSmallIntegerField(verbose_name='Meses del corte')),
            ],
        ),
    ]
