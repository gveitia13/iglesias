from django.contrib import admin

from app_main.models import Distrito, Presbiterio


# Register your models here.
@admin.register(Distrito)
class DistritoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Datos personales',
         {'fields': ('nombre', 'apellidos', 'distrito', 'fecha')}),
        ('Cuerpo Ministerial',
         {'fields': ('presbiteriales', 'nacionales', 'licenciados', 'ordenados', 'total_cuerpo_ministerial')}),
        ('Patrimonio de la organización',
         {'fields': ('templos_oficiales', 'templos_no_oficiales', 'casa_templo', 'tabernaculos', 'casas_pastorales')}),
        ('Congregaciones / Lugares de predicación',
         {'fields': ('iglesias', 'misiones', 'casas_cultos',)}),
        ('Afiliación oficial',
         {'fields': ('ministros', 'miembros', 'visitantes', 'ninnos', 'total_afiliacion_oficial')}),
        ('Departamentos / Ministerios',
         {'fields': ('jovenes', 'damas', 'caballeros',)}),
        ('Liderazgo / Estudios Teológicos',
         {'fields': ('lideres_locales', 'obreros_tiempo_completo', 'estudiantes')}),
        ('Asistencia / Bautizos',
         {'fields': ('promedio_asistencia', 'bautizados_espiritu',)}),
    ]
    readonly_fields = ('fecha', 'total_cuerpo_ministerial', 'total_afiliacion_oficial', 'bautizados_espiritu',
                       'promedio_asistencia')

    search_fields = ('presbiterio', 'fecha')
    list_filter = ('distrito', 'fecha')


@admin.register(Presbiterio)
class PresbiterioAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Datos personales',
         {'fields': ('nombre', 'apellidos', 'distrito', 'presbiterio', 'fecha')}),
        ('Cuerpo Ministerial',
         {'fields': ('presbiteriales', 'nacionales', 'licenciados', 'ordenados', 'total_cuerpo_ministerial')}),
        ('Patrimonio de la organización',
         {'fields': ('templos_oficiales', 'templos_no_oficiales', 'casa_templo', 'tabernaculos', 'casas_pastorales')}),
        ('Congregaciones / Lugares de predicación',
         {'fields': ('iglesias', 'misiones', 'casas_cultos',)}),
        ('Afiliación oficial',
         {'fields': ('ministros', 'miembros', 'visitantes', 'ninnos', 'total_afiliacion_oficial')}),
        ('Departamentos / Ministerios',
         {'fields': ('jovenes', 'damas', 'caballeros',)}),
        ('Liderazgo / Estudios Teológicos',
         {'fields': ('lideres_locales', 'obreros_tiempo_completo', 'estudiantes')}),
        ('Asistencia / Bautizos',
         {'fields': ('promedio_asistencia', 'bautizados_espiritu',)}),
    ]
    readonly_fields = ('fecha', 'total_cuerpo_ministerial', 'total_afiliacion_oficial', 'bautizados_espiritu',
                       'promedio_asistencia')

    search_fields = ('presbiterio', 'fecha')
    list_filter = ('distrito', 'fecha')
