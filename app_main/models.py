from crum import get_current_user
from django.db import models

from iglesias import settings


class Distrito(models.Model):
    nombre = models.CharField('Nombre', max_length=100)
    apellidos = models.CharField('Apellidos', max_length=100)
    distrito = models.CharField('Distrito', max_length=100, null=True, blank=True)
    fecha = models.DateField('Fecha de creación', auto_now_add=True, )
    # Cuerpo ministerial
    presbiteriales = models.PositiveIntegerField()
    nacionales = models.PositiveIntegerField()
    licenciados = models.PositiveIntegerField()
    ordenados = models.PositiveIntegerField()
    total_cuerpo_ministerial = models.PositiveIntegerField(blank=True, null=True)
    # Patrimonio de la organization
    templos_oficiales = models.PositiveIntegerField()
    templos_no_oficiales = models.PositiveIntegerField()
    casa_templo = models.PositiveIntegerField()
    tabernaculos = models.PositiveIntegerField('Tabernáculos/Naves')
    casas_pastorales = models.PositiveIntegerField()
    # Congregaciones / Lugares de predicación
    iglesias = models.PositiveIntegerField()
    misiones = models.PositiveIntegerField()
    casas_cultos = models.PositiveIntegerField('Casas Cultos/Células')
    # Afiliacion oficial
    ministros = models.PositiveIntegerField()
    miembros = models.PositiveIntegerField()
    visitantes = models.PositiveIntegerField()
    ninnos = models.PositiveIntegerField('Niños')
    total_afiliacion_oficial = models.PositiveIntegerField('Total afiliación oficial')
    # Departamentos / Ministerios
    jovenes = models.PositiveIntegerField('Jóvenes')
    damas = models.PositiveIntegerField()
    caballeros = models.PositiveIntegerField()
    # Aistencia / Bautizados
    promedio_asistencia = models.FloatField()
    bautizados_espiritu = models.FloatField('Bautizados Espíritu')
    # Liderazgo / Estudios Teológicos
    lideres_locales = models.PositiveIntegerField('Líderes locales')
    obreros_tiempo_completo = models.PositiveIntegerField()
    estudiantes = models.PositiveIntegerField()

    def __str__(self):
        return f'Distrito - {self.nombre} {self.apellidos}: {self.fecha}'


class Presbiterio(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    nombre = models.CharField('Nombre', max_length=100)
    apellidos = models.CharField('Apellidos', max_length=100)
    distrito = models.ForeignKey('Distrito', on_delete=models.CASCADE, null=True, blank=True)

    fecha = models.DateField('Fecha de creación', auto_now_add=True, )
    presbiterio = models.CharField(null=True, blank=True, max_length=500)
    # Cuerpo ministerial
    presbiteriales = models.PositiveIntegerField()
    nacionales = models.PositiveIntegerField()
    licenciados = models.PositiveIntegerField()
    ordenados = models.PositiveIntegerField()
    total_cuerpo_ministerial = models.PositiveIntegerField(blank=True, null=True)
    # Patrimonio de la organization
    templos_oficiales = models.PositiveIntegerField()
    templos_no_oficiales = models.PositiveIntegerField()
    casa_templo = models.PositiveIntegerField()
    tabernaculos = models.PositiveIntegerField('Tabernáculos/Naves')
    casas_pastorales = models.PositiveIntegerField()
    # Congregaciones / Lugares de predicación
    iglesias = models.PositiveIntegerField()
    misiones = models.PositiveIntegerField()
    casas_cultos = models.PositiveIntegerField('Casas Cultos/Células')
    # Afiliacion oficial
    ministros = models.PositiveIntegerField()
    miembros = models.PositiveIntegerField()
    visitantes = models.PositiveIntegerField()
    ninnos = models.PositiveIntegerField('Niños')
    total_afiliacion_oficial = models.PositiveIntegerField('Total afiliación oficial')
    # Departamentos / Ministerios
    jovenes = models.PositiveIntegerField('Jóvenes')
    damas = models.PositiveIntegerField()
    caballeros = models.PositiveIntegerField()
    # Aistencia / Bautizados
    promedio_asistencia = models.FloatField()
    bautizados_espiritu = models.FloatField('Bautizados Espíritu')
    # Liderazgo / Estudios Teológicos
    lideres_locales = models.PositiveIntegerField('Líderes locales')
    obreros_tiempo_completo = models.PositiveIntegerField()
    estudiantes = models.PositiveIntegerField()

    def __str__(self):
        return f'Presbiterio - {self.nombre} {self.apellidos}: {self.fecha}'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        # self.full_clean()
        user = get_current_user()
        if not self.user:
            self.user = user
        return super().save()
