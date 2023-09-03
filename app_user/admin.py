from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from app_user.forms import UserForm, MyUserCreationForm, MyUserAuthenticationForm
from app_user.models import User


# Register your models here.
class MyUserAdmin(UserAdmin):
    fieldsets = [
        (None, {"fields": ("username", "email", "password", 'distrito')}),
        (_("Personal info"), {"fields": ("first_name", "last_name", 'image', 'get_image')}),
        ('Permisos', {"fields":
            (
                "is_active",
                'is_superstar',
                'role',
            ), },),
        ('Fechas importantes', {"fields": ("last_login", "date_joined")}),
    ]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", 'email', "password1", "password2",),
            },
        ),
    )
    readonly_fields = ['last_login', 'date_joined', 'get_image', 'distrito']
    list_display = ('get_image', 'distrito', "username", "email", 'role', 'is_active')
    list_display_links = ('get_image', "username", 'distrito')
    list_filter = ("is_active", 'role',)
    search_fields = ("username", "first_name", "last_name", "email",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )
    actions = ['Activar_Usuarios', 'Desactivar_Usuarios']
    ordering = ('-is_superstar', '-is_active')
    form = UserForm
    add_form = MyUserCreationForm

    def get_readonly_fields(self, request, obj=None):
        read_only = super().get_readonly_fields(request, obj)
        if request.user.is_superstar:
            read_only = [r for r in read_only if r != 'distrito']
        return read_only

    def has_add_permission(self, request):
        if bool(request.user and not request.user.is_superstar):
            return False
        return True

    def has_change_permission(self, request, obj=None):
        if bool(request.user and request.user.is_superstar):
            return True
        if obj == request.user:
            return True
        return False

    def get_fieldsets(self, request, obj=None):
        fields = super().get_fieldsets(request, obj)
        if not request.user.is_superstar:
            fields = [f for f in fields if f[0] != 'Permisos' and f[0] != 'Fechas importantes']
        return fields

    def has_view_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        if bool(request.user and request.user.is_superstar):
            return True
        if obj == request.user:
            return True
        return False

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if bool(request.user and not request.user.is_superstar):
            return qs.filter(is_superstar=False)
        return qs

    def get_list_display(self, request):
        list = super().get_list_display(request)
        if not request.user.is_anonymous and request.user.is_superstar:
            list += ('is_superstar',)
        return list

    def Desactivar_Usuarios(self, request, queryset):
        cnt = queryset.filter(is_active=True).update(is_active=False)
        self.message_user(request, '{} usuarios desactivados.'.format(cnt), messages.WARNING)

    def Activar_Usuarios(self, request, queryset):
        cnt = queryset.filter(is_active=False).update(is_active=True)
        self.message_user(request, '{} usuarios activados.'.format(cnt), messages.SUCCESS)

    def get_actions(self, request):
        actions = super().get_actions(request)
        if not request.user.is_superstar:
            del actions['Activar_Usuarios']
            del actions['Desactivar_Usuarios']
        return actions


admin.site.register(User, MyUserAdmin)
admin.site.unregister(Group)
admin.site.login_form = MyUserAuthenticationForm

# @admin.register(Group)
# class MyGroupAdmin(GroupAdmin):
#     def has_module_permission(self, request):
#         if not request.user.is_anonymous and request.user.is_superstar:
#             return True
#         return False
