from typing import Any

from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.conf import settings
from django.http import HttpRequest


class AccountAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request: HttpRequest):
        return getattr(settings, "ACCOUNT_ALLOW_REGISTRATION", True)


class CustomAccountAdapter(AccountAdapter):
    def get_email_confirmation_url(self, request, emailconfirmation):
        activation_url = getattr(settings, "ACCOUNT_ACTIVATION_LINK", None)

        """
        Constructs the email confirmation (activation) url.
        If activation url is not configured defaults django-allauth implementation
        """
        return (
            super().get_email_confirmation_url(request, emailconfirmation)
            if activation_url is None
            else f"{activation_url}{emailconfirmation.key}/"
        )


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def is_open_for_signup(self, request: HttpRequest, sociallogin: Any):
        return getattr(settings, "ACCOUNT_ALLOW_REGISTRATION", True)
