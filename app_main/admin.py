from django.contrib import admin
from django.db.models import QuerySet

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
    readonly_fields = (
        'fecha', 'total_cuerpo_ministerial', 'total_afiliacion_oficial', 'cant_presbiterios', 'total_departamento')

    search_fields = ('presbiterio', 'fecha')
    list_filter = ('distrito', 'fecha')
    list_display = ('distrito', 'cant_presbiterios', 'nombre', 'apellidos', 'fecha', 'get_options')
    list_display_links = None

    def has_add_permission(self, request):
        return bool(request.user and (request.user.is_superstar or request.user.role == '1'))

    # def has_change_permission(self, request, obj=None):
    #     return bool(request.user and obj and (
    #             request.user.is_superstar or (
    #             request.user.role == '1' and obj.user == request.user)))
    #
    # def has_delete_permission(self, request, obj=None):
    #     return bool(request.user and obj and (
    #             request.user.is_superstar or (
    #             request.user.role == '1' and obj.user == request.user)))

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superstar:
            return queryset
        if request.user.role == '2':
            from app_user.models import User
            return queryset.filter()

        return queryset


@admin.register(Presbiterio)
class PresbiterioAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Datos personales',
         {'fields': ('get_distrito', 'nombre', 'apellidos', 'presbiterio', 'fecha')}),
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
    readonly_fields = (
        'get_distrito', 'fecha', 'total_cuerpo_ministerial', 'total_afiliacion_oficial', 'total_departamento')

    search_fields = ('presbiterio', 'fecha')
    list_filter = ('fecha',)
    list_display = ('get_distrito', 'presbiterio', 'user', 'nombre', 'apellidos', 'fecha', 'get_options')
    list_display_links = None

    def has_change_permission(self, request, obj=None):
        if bool(request.user and obj and (
                request.user.is_superstar or request.user.role == '1' or (
                request.user.role == '2' and obj.user == request.user))):
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if bool(request.user and obj and (
                request.user.is_superstar or request.user.role == '1' or (
                request.user.role == '2' and obj.user == request.user))):
            return True
        return False

    # def get_queryset(self, request):
    #     queryset = super().get_queryset(request)
    #     if request.user.is_superstar:
    #         return queryset
    #     if request.user.role == '1':
    #         distritos = Distrito.objects.filter(user_id=request.user)
    #         return queryset.filter(distrito__in=distritos).distinct()
    #     return queryset.filter(user=request.user)
