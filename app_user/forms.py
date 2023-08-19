from django.contrib.admin.forms import AdminAuthenticationForm
from django.contrib.auth.forms import UserChangeForm, ReadOnlyPasswordHashField, UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from app_user.models import User


class UserForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if not isinstance(self.fields[field], ReadOnlyPasswordHashField):
                self.fields[field].widget.attrs.update({'class': 'form-control'})


class MyUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class MyUserAuthenticationForm(AdminAuthenticationForm):
    error_messages = {
        "invalid_login": _(
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        "inactive": _("This account is inactive."),
    }

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise ValidationError(
                self.error_messages["inactive"],
                code="inactive",
            )
        if not user.is_staff:
            raise ValidationError(
                self.error_messages["invalid_login"],
                code="invalid_login",
                params={"username": self.username_field.verbose_name},
            )
        # super().confirm_login_allowed(user)
