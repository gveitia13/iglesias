from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from app_user.forms import UserForm, MyUserCreationForm
from app_user.models import User


# Register your models here.
@admin.register(User)
class MyUserAdmin(UserAdmin):
    fieldsets = [
        (None, {"fields": ("username", "email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name",)}),
        ('Permisos', {"fields":
            (
                "is_active",
                'is_distro',
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
    readonly_fields = ('last_login', 'date_joined',)
    list_display = (
        "username", "first_name", "last_name", "email", 'is_active')
    list_display_links = ("username",)
    list_filter = ("is_active",)
    search_fields = ("username", "first_name", "last_name", "email",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )
    actions = ['Activar_Usuarios', 'Desactivar_Usuarios']
    ordering = ('-is_distro', '-is_active')
    form = UserForm
    add_form = MyUserCreationForm

    def has_add_permission(self, request):
        if bool(request.user and not request.user.is_distro):
            return False
        return True

    def has_change_permission(self, request, obj=None):
        if bool(request.user and request.user.is_distro):
            return True
        if obj == request.user:
            return True
        return False

    def get_fieldsets(self, request, obj=None):
        fields = super().get_fieldsets(request, obj)
        if not request.user.is_distro:
            fields = [f for f in fields if f[0] != 'Permisos' and f[0] != 'Fechas importantes']
        return fields

    def has_view_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        if bool(request.user and request.user.is_distro):
            return True
        if obj == request.user:
            return True
        return False

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if bool(request.user and not request.user.is_distro):
            return qs.filter(is_superstar=False)
        return qs

    def get_list_display(self, request):
        list = super().get_list_display(request)
        if not request.user.is_anonymous and request.user.is_distro:
            list += ('is_distro',)
        return list

    def Desactivar_Usuarios(self, request, queryset):
        cnt = queryset.filter(is_active=True).update(is_active=False)
        self.message_user(request, '{} usuarios desactivados.'.format(cnt), messages.WARNING)

    def Activar_Usuarios(self, request, queryset):
        cnt = queryset.filter(is_active=False).update(is_active=True)
        self.message_user(request, '{} usuarios activados.'.format(cnt), messages.SUCCESS)

    def get_actions(self, request):
        actions = super().get_actions(request)
        if not request.user.is_distro:
            del actions['Activar_Usuarios']
            del actions['Desactivar_Usuarios']
        return actions


admin.site.unregister(Group)


@admin.register(Group)
class MyGroupAdmin(GroupAdmin):
    def has_module_permission(self, request):
        if not request.user.is_anonymous and request.user.is_distro:
            return True
        return False
