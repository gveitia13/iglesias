from django.contrib import admin

from app_main.models import Distrito, Presbiterio


# Register your models here.
@admin.register(Distrito)
class DistritoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Datos personales',
         {'fields': ('nombre', 'apellidos', 'distrito', 'fecha', 'cant_presbiterios')}),
        ('Cuerpo Ministerial',
         {'fields': ('presbiteriales', 'nacionales', 'licenciados', 'ordenados', 'total_cuerpo_ministerial')}),
        ('Patrimonio de la organización',
         {'fields': ('templos_oficiales', 'templos_no_oficiales', 'casa_templo', 'tabernaculos', 'casas_pastorales')}),
        ('Congregaciones / Lugares de predicación',
         {'fields': ('iglesias', 'misiones', 'casas_cultos',)}),
        ('Afiliación oficial',
         {'fields': ('ministros', 'miembros', 'visitantes', 'ninnos', 'total_afiliacion_oficial')}),
        ('Departamentos / Ministerios',
         {'fields': ('jovenes', 'damas', 'caballeros', 'total_departamento')}),
        ('Liderazgo / Estudios Teológicos',
         {'fields': ('lideres_locales', 'obreros_tiempo_completo', 'estudiantes')}),
        ('Asistencia / Bautizos',
         {'fields': ('promedio_asistencia', 'bautizados_espiritu',)}),
    ]
    readonly_fields = ('fecha', 'total_cuerpo_ministerial', 'total_afiliacion_oficial', 'bautizados_espiritu',
                       'promedio_asistencia', 'cant_presbiterios', 'total_departamento')

    search_fields = ('presbiterio', 'fecha')
    list_filter = ('distrito', 'fecha')

    def has_add_permission(self, request):
        if bool(request.user and (request.user.is_superstar or request.user.role == '1')):
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if bool(request.user and (request.user.is_superstar or request.user.role == '1')):
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if bool(request.user and (request.user.is_superstar or request.user.role == '1')):
            return True
        return False


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
         {'fields': ('jovenes', 'damas', 'caballeros', 'total_departamento')}),
        ('Liderazgo / Estudios Teológicos',
         {'fields': ('lideres_locales', 'obreros_tiempo_completo', 'estudiantes')}),
        ('Asistencia / Bautizos',
         {'fields': ('promedio_asistencia', 'bautizados_espiritu',)}),
    ]
    readonly_fields = ('fecha', 'total_cuerpo_ministerial', 'total_afiliacion_oficial', 'bautizados_espiritu',
                       'promedio_asistencia', 'total_departamento')

    search_fields = ('presbiterio', 'fecha')
    list_filter = ('distrito', 'fecha')

    def has_change_permission(self, request, obj=None):
        if bool(request.user and obj and (
                request.user.is_superstar or (request.user.role == '2' and obj.user == request.user))):
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if bool(request.user and obj and (
                request.user.is_superstar or (request.user.role == '2' and obj.user == request.user))):
            return True
        return False

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.filter(user=request.user)
        return queryset
