from django.contrib import admin

from app_main.models import Distrito, Presbiterio, ResumenDistrito


# Register your models here.
@admin.register(Distrito)
class DistritoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Datos personales',
         {'fields': ('nombre', 'apellidos', 'distrito', 'fecha', 'cant_presbiterios', 'evaluado')}),
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
    readonly_fields = ('fecha', 'total_cuerpo_ministerial', 'total_afiliacion_oficial', 'cant_presbiterios',
                       'total_departamento', 'presbiteriales', 'nacionales', 'licenciados', 'ordenados',
                       'total_cuerpo_ministerial', 'templos_oficiales', 'templos_no_oficiales', 'casa_templo',
                       'tabernaculos', 'casas_pastorales', 'iglesias', 'misiones', 'casas_cultos', 'ministros',
                       'miembros', 'visitantes', 'ninnos', 'total_afiliacion_oficial', 'jovenes', 'damas', 'caballeros',
                       'total_departamento', 'promedio_asistencia', 'bautizados_espiritu', 'lideres_locales',
                       'obreros_tiempo_completo', 'estudiantes', 'evaluado')

    search_fields = ('presbiterio', 'fecha')
    list_filter = ('distrito', 'fecha')
    list_display = ('distrito', 'cant_presbiterios', 'nombre', 'apellidos', 'fecha', 'evaluado', 'get_options')
    list_display_links = None
    change_list_template = 'admin/distrito_change_list.html'

    def has_add_permission(self, request):
        return bool(request.user and request.user.is_superstar)

    def has_change_permission(self, request, obj=None):
        user = request.user
        if bool(user and obj and user.is_superstar):
            return True
        if obj and (user in obj.user_set.all()) and user.role == '1':
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        user = request.user
        if bool(user and obj and user.is_superstar):
            return True
        if obj and (user in obj.user_set.all()) and user.role == '1':
            return True
        return False

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superstar:
            return queryset
        return queryset.filter(user=request.user)


@admin.register(Presbiterio)
class PresbiterioAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Datos personales',
         {'fields': ('get_distrito', 'nombre', 'apellidos', 'presbiterio', 'evaluado', 'fecha')}),
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
        'get_distrito', 'fecha', 'total_cuerpo_ministerial', 'total_afiliacion_oficial', 'total_departamento',
        'evaluado')

    search_fields = ('presbiterio', 'fecha')
    list_filter = ('fecha',)
    list_display = ('get_distrito', 'presbiterio', 'user', 'nombre', 'apellidos', 'fecha', 'evaluado', 'get_options')
    list_display_links = None

    def has_add_permission(self, request):
        if request.user.role == '2' and request.user.distrito:
            return True
        return False

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        user = request.user
        if user.is_superstar:
            return qs
        if (user.role == '2' or user.role == '1') and user.distrito:
            distrito = user.distrito
            users = distrito.user_set.all()
            qs = qs.filter(user__in=users)
        else:
            qs = qs.none()
        return qs

    def has_change_permission(self, request, obj=None):
        if obj and obj.evaluado:
            return False
        if bool(request.user and obj and (request.user.is_superstar or (
                request.user.role == '2' and obj.user == request.user))):
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if bool(request.user and obj and (request.user.is_superstar or (
                request.user.role == '2' and obj.user == request.user))):
            return True
        return False


@admin.register(ResumenDistrito)
class ResumenDistritoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Principal', {'fields': ('distrito', 'fecha', 'fecha_resumen', 'cant_presbiterios', 'cantidad_meses')}),
        ('Datos personales',
         {'fields': ('nombre', 'apellidos', 'user')}),
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
    list_display = ('__str__', 'user', 'fecha_resumen', 'cantidad_meses', 'get_options')
    readonly_fields = [attr for attr in ResumenDistrito.__dict__.keys()]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        user = request.user
        if bool(user and obj and user.is_superstar):
            return True
        if obj and (obj.user == user):
            return True
        return False

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        user = request.user
        return qs if user.is_superstar else qs.filter(user=user)

    def has_view_permission(self, request, obj=None):
        user = request.user
        if bool(user and (user.is_superstar or user.role == '1')):
            return True
        return False
