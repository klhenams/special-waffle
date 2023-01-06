from allauth.account.adapter import get_adapter
from allauth.account.forms import ResetPasswordForm, SignupForm
from allauth.account.utils import user_pk_to_url_str
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from allauth.utils import build_absolute_uri
from django.conf import settings
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserAdminChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserAdminCreationForm(admin_forms.UserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

        error_messages = {
            "username": {"unique": _("This username has already been taken.")}
        }


class UserSignupForm(SignupForm):
    """
    Form that will be rendered on a user sign up section/screen.
    Default fields will be added automatically.
    Check UserSocialSignupForm for accounts created from social.
    """


class UserSocialSignupForm(SocialSignupForm):
    """
    Renders the form when user has signed up using social accounts.
    Default fields will be added automatically.
    See UserSignupForm otherwise.
    """


class CustomResetPasswordForm(ResetPasswordForm):
    def _send_password_reset_mail(self, request, email, users, **kwargs):
        reset_url = getattr(settings, "PASSWORD_RESET_LINK", None)
        token_generator = kwargs.get("token_generator")

        for user in users:

            temp_key = token_generator.make_token(user)
            uid = user_pk_to_url_str(user)

            url = f"{reset_url}{uid}/{temp_key}/"

            if reset_url is None:
                path = reverse(
                    "account_reset_password_from_key",
                    kwargs=dict(uidb36=uid, key=temp_key),
                )
                url = build_absolute_uri(request, path)

            context = {
                "user": user,
                "password_reset_url": url,
                "request": request,
            }
            get_adapter(request).send_mail(
                "account/email/password_reset_key", email, context
            )
