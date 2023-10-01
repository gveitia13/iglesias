from datetime import datetime

from crum import get_current_user
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.safestring import mark_safe

from iglesias import settings


class Distrito(models.Model):
    nombre = models.CharField('Nombre', max_length=100)
    apellidos = models.CharField('Apellidos', max_length=100)
    distrito = models.CharField('Distrito', max_length=100, null=True, blank=True)
    fecha = models.DateField('Fecha de creación', auto_now_add=True,
                             help_text='Se autosignará la fecha cuando sea creado')
    cant_presbiterios = models.PositiveIntegerField('Cantidad de presbiterios', default=0, null=True, blank=True)
    # Cuerpo ministerial
    presbiteriales = models.PositiveIntegerField(default=0)
    nacionales = models.PositiveIntegerField(default=0)
    licenciados = models.PositiveIntegerField(default=0)
    ordenados = models.PositiveIntegerField(default=0)
    total_cuerpo_ministerial = models.PositiveIntegerField(blank=True, null=True)
    # Patrimonio de la organization
    templos_oficiales = models.PositiveIntegerField(default=0)
    templos_no_oficiales = models.PositiveIntegerField(default=0)
    casa_templo = models.PositiveIntegerField(default=0)
    tabernaculos = models.PositiveIntegerField('Tabernáculos/Naves', default=0)
    casas_pastorales = models.PositiveIntegerField(default=0)
    # Congregaciones / Lugares de predicación
    iglesias = models.PositiveIntegerField(default=0)
    misiones = models.PositiveIntegerField(default=0)
    casas_cultos = models.PositiveIntegerField('Casas Cultos/Células', default=0)
    # Afiliacion oficial
    ministros = models.PositiveIntegerField(default=0)
    miembros = models.PositiveIntegerField(default=0)
    visitantes = models.PositiveIntegerField(default=0)
    ninnos = models.PositiveIntegerField('Niños', default=0)
    total_afiliacion_oficial = models.PositiveIntegerField('Total afiliación oficial', default=0)
    # Departamentos / Ministerios
    jovenes = models.PositiveIntegerField('Jóvenes', default=0)
    damas = models.PositiveIntegerField(default=0)
    caballeros = models.PositiveIntegerField(default=0)
    total_departamento = models.PositiveIntegerField('Total Departamento / Ministerios', help_text='Incluye niños',
                                                     default=0)
    # Aistencia / Bautizados
    promedio_asistencia = models.FloatField(null=True, blank=True, default=0,
                                            validators=[MinValueValidator(0, 'Debe ser mayor o igual a cero')])
    bautizados_espiritu = models.FloatField('Bautizados Espíritu', null=True, blank=True, default=0,
                                            validators=[MinValueValidator(0, 'Debe ser mayor o igual a cero')])
    # Liderazgo / Estudios Teológicos
    lideres_locales = models.PositiveIntegerField('Líderes locales', default=0)
    obreros_tiempo_completo = models.PositiveIntegerField(default=0)
    estudiantes = models.PositiveIntegerField(default=0)
    evaluado = models.BooleanField(default=False)

    # def get_cant_presbiterios(self):
    #     return self.presbiterio_set.count()

    def __str__(self):
        return f'{self.distrito}'

    def get_options(self):
        user = get_current_user()
        html = f'<a href="/admin/app_main/distrito/{self.pk}/change/" class="btn m-1 btn-sm btn-warning"><i ' \
               f'class="fas fa-edit"></i></a>'
        if user.is_superstar or (user in self.user_set.all() and user.role == '1'):
            html += f'<a href="/admin/app_main/distrito/{self.pk}/delete/" class="btn m-1 btn-sm btn-danger"><i ' \
                    f'class="fas fa-trash-alt"></i></a>'
        html = '<div class="d-flex">' + html + '</div>'
        return mark_safe(html)

    get_options.short_description = 'Opciones'

    # get_cant_presbiterios.short_description = 'Cantidad de presbiterios'

    class Meta:
        ordering = ('distrito',)


class Presbiterio(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuario', on_delete=models.CASCADE, null=True,
                             blank=True)
    nombre = models.CharField('Nombre', max_length=100)
    apellidos = models.CharField('Apellidos', max_length=100)
    # distrito = models.ForeignKey('Distrito', on_delete=models.CASCADE, null=True, blank=True)

    fecha = models.DateField('Fecha de creación', auto_now_add=True,
                             help_text='Se autosignará la fecha cuando sea creado')
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
    total_departamento = models.PositiveIntegerField('Total Departamento / Ministerios', help_text='Incluye niños')
    # Aistencia / Bautizados
    promedio_asistencia = models.FloatField(null=True, blank=True,
                                            validators=[MinValueValidator(0, 'Debe ser mayor o igual a cero')])
    bautizados_espiritu = models.FloatField('Bautizados Espíritu', null=True, blank=True,
                                            validators=[MinValueValidator(0, 'Debe ser mayor o igual a cero')])
    # Liderazgo / Estudios Teológicos
    lideres_locales = models.PositiveIntegerField('Líderes locales')
    obreros_tiempo_completo = models.PositiveIntegerField()
    estudiantes = models.PositiveIntegerField()
    evaluado = models.BooleanField(default=False)

    def __str__(self):
        return f'Presbiterio - {self.presbiterio}: {self.fecha}'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        # self.full_clean()
        user = get_current_user()
        if not self.user:
            self.user = user
        self.total_cuerpo_ministerial = self.presbiteriales + self.nacionales + self.licenciados + self.ordenados
        self.total_afiliacion_oficial = self.ministros + self.miembros + self.visitantes + self.ninnos
        self.total_departamento = self.jovenes + self.damas + self.caballeros + self.ninnos
        return super().save()

    def get_options(self):
        user = get_current_user()
        html = f'<div class="d-flex"><a href="/admin/app_main/presbiterio/{self.pk}/change/" ' \
               f'class="btn m-1 btn-sm btn-warning"><i class="fas fa-edit"></i></a>'

        if user.is_superstar or (user.role == '2' and self.user == user):
            html += f'<a href="/admin/app_main/presbiterio/{self.pk}/delete/" ' \
                    f'class="btn m-1 btn-sm btn-danger"><i class="fas fa-trash-alt"></i></a></div>'
        html = '<div class="d-flex">' + html + '</div>'
        return mark_safe(html)

    def get_distrito(self):
        if self.user:
            return self.user.distrito
        user = get_current_user()
        return user.distrito

    get_options.short_description = 'Opciones'
    get_distrito.short_description = 'Distrito'

    class Meta:
        ordering = ('user',)


class ResumenDistrito(models.Model):
    nombre = models.CharField('Nombre', max_length=100)
    apellidos = models.CharField('Apellidos', max_length=100)
    distrito = models.CharField('Distrito', max_length=100, null=True, blank=True)
    fecha = models.DateField('Fecha del Distrito')
    fecha_resumen = models.DateField('Fecha del Resumen', auto_now_add=True, )
    cant_presbiterios = models.PositiveIntegerField('Cantidad de presbiterios', default=0, null=True, blank=True)
    # Cuerpo ministerial
    presbiteriales = models.PositiveIntegerField(default=0)
    nacionales = models.PositiveIntegerField(default=0)
    licenciados = models.PositiveIntegerField(default=0)
    ordenados = models.PositiveIntegerField(default=0)
    total_cuerpo_ministerial = models.PositiveIntegerField(blank=True, null=True)
    # Patrimonio de la organization
    templos_oficiales = models.PositiveIntegerField(default=0)
    templos_no_oficiales = models.PositiveIntegerField(default=0)
    casa_templo = models.PositiveIntegerField(default=0)
    tabernaculos = models.PositiveIntegerField('Tabernáculos/Naves', default=0)
    casas_pastorales = models.PositiveIntegerField(default=0)
    # Congregaciones / Lugares de predicación
    iglesias = models.PositiveIntegerField(default=0)
    misiones = models.PositiveIntegerField(default=0)
    casas_cultos = models.PositiveIntegerField('Casas Cultos/Células', default=0)
    # Afiliacion oficial
    ministros = models.PositiveIntegerField(default=0)
    miembros = models.PositiveIntegerField(default=0)
    visitantes = models.PositiveIntegerField(default=0)
    ninnos = models.PositiveIntegerField('Niños', default=0)
    total_afiliacion_oficial = models.PositiveIntegerField('Total afiliación oficial', default=0)
    # Departamentos / Ministerios
    jovenes = models.PositiveIntegerField('Jóvenes', default=0)
    damas = models.PositiveIntegerField(default=0)
    caballeros = models.PositiveIntegerField(default=0)
    total_departamento = models.PositiveIntegerField('Total Departamento / Ministerios', help_text='Incluye niños',
                                                     default=0)
    # Aistencia / Bautizados
    promedio_asistencia = models.FloatField(null=True, blank=True, default=0,
                                            validators=[MinValueValidator(0, 'Debe ser mayor o igual a cero')])
    bautizados_espiritu = models.FloatField('Bautizados Espíritu', null=True, blank=True, default=0,
                                            validators=[MinValueValidator(0, 'Debe ser mayor o igual a cero')])
    # Liderazgo / Estudios Teológicos
    lideres_locales = models.PositiveIntegerField('Líderes locales', default=0)
    obreros_tiempo_completo = models.PositiveIntegerField(default=0)
    estudiantes = models.PositiveIntegerField(default=0)
    cantidad_meses = models.PositiveSmallIntegerField('Meses del corte')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
                             verbose_name='Superintendente')

    def __str__(self):
        return f'Resumen del {self.distrito}'

    def get_options(self):
        user = get_current_user()
        # html = f'<a href="/web/pdf_reporte/{self.pk}/" class="btn m-1 btn-sm btn-info"><i ' \
        #        f'class="fas fa-file-pdf"></i> PDF</a>'
        html = f'<a href="/web/print_reporte/{self.pk}/" class="btn m-1 btn-sm btn-info"><i ' \
                f'class="fas fa-print"></i> Imprimir</a>'
        if self.user == user or user.is_superstar:
            html += f'<a href="/admin/app_main/resumendistrito/{self.pk}/delete/" class="btn m-1 btn-sm btn-danger"><i ' \
                    f'class="fas fa-trash-alt"></i></a>'
        html = '<div class="d-flex">' + html + '</div>'
        return mark_safe(html)

    get_options.short_description = 'Opciones'
