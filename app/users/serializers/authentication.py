from dj_rest_auth.serializers import PasswordResetSerializer

from ..forms import CustomResetPasswordForm


class CustomPasswordResetSerializer(PasswordResetSerializer):
    @property
    def password_reset_form_class(self):
        return CustomResetPasswordForm
