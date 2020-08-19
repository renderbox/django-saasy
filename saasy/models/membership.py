from django.db import models
from django.apps import apps
from django.utils.translation import gettext_lazy as _

config = apps.get_app_config('saasy')

class Membership(models.Model):

    profile = models.ForeignKey(config.PROFILE_MODEL, verbose_name=_("User Profile"), on_delete=models.CASCADE, related_name="memberships")
    organization = models.ForeignKey(config.ORGANIZATION_MODEL, verbose_name=_("Organization"), on_delete=models.CASCADE, related_name="memberships")
    uuid = models.UUIDField(_("UUID"))

    class Meta:
        verbose_name = _("Membership")
        verbose_name_plural = _("Memberships")

    # def __str__(self):
    #     return self.name
