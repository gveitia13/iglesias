from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from app_main.models import Distrito
from iglesias.settings import STATIC_URL


class User(AbstractUser):
    email = models.EmailField(_("email address"), null=True, blank=True, unique=True)
    is_superstar = models.BooleanField(
        _("Admin"), default=False, help_text=_("Designates that this user has all permissions without "
                                               "explicitly assigning them."), )
    is_superuser = models.BooleanField(
        _("superuser status"), default=True, help_text=_(
            "Designates that this user has all permissions without "
            "explicitly assigning them."
        ), )
    is_staff = models.BooleanField(
        _("staff status"), default=True, help_text=_("Designates whether the user can log into this admin site."), )
    role = models.CharField('Rol', choices=(
        ('1', 'Superintendente '),
        ('2', 'Presbítero'),
    ), max_length=2, null=True, blank=True)
    image = models.ImageField('Foto de perfil', null=True, blank=True, upload_to='user/')
    distrito = models.ForeignKey(Distrito, on_delete=models.SET_NULL, null=True, blank=True)
    REQUIRED_FIELDS = ['is_superstar', 'email']

    class Meta:
        verbose_name = 'Usuario'
        ordering = ('-is_superstar', '-is_active')

    def get_image(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" class="img-fluid rounded-pill" '
                             f'style="height:50px;width:50px;"> </img>')
        return mark_safe(
            f'<img src="{STATIC_URL}admin/img/unknown.png" class="img-fluid rounded-pill" '
            f'style="height:50px;width:50px;"> </img>')

    def get_image_url(self):
        if self.image:
            return self.image.url
        return STATIC_URL + 'admin/img/unknown.png'

    get_image.short_description = 'Foto de perfil'

    def __str__(self):
        return self.username
