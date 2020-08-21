import uuid

from django.db import models
from django.apps import apps
from django.utils.translation import gettext_lazy as _


class Membership(models.Model):
    
    profile = models.ForeignKey('saasy.SaasyProfile', verbose_name=_("User Profile"), on_delete=models.CASCADE, related_name="memberships")
    organization = models.ForeignKey('saasy.Organization', verbose_name=_("Organization"), on_delete=models.CASCADE, related_name="memberships")
    uuid = models.UUIDField(_("UUID"), default=uuid.uuid4, editable=False, unique=True)
    role = models.ForeignKey('saasy.Role', verbose_name=_("Role"), on_delete=models.CASCADE, related_name="memberships")
    
    class Meta:
        verbose_name = _("Membership")
        verbose_name_plural = _("Memberships")

    def __str__(self):
        return self.organization.name + "::" + self.profile.slug
