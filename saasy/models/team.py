import uuid

from django.conf import settings
from django.contrib.sites.models import Site
from django.db import models
from django.apps import apps
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from autoslug import AutoSlugField


class Team(models.Model):

    name = models.CharField(_("Name"), max_length=80, blank=True)
    slug = AutoSlugField(populate_from='name', unique=True, always_update=True)                                                                         # Gets set in the save
    organization = models.ForeignKey('saasy.Organization', verbose_name=_("Organization"), on_delete=models.CASCADE, related_name="teams")
    members = models.ManyToManyField('saasy.Membership', verbose_name=_("Members"), related_name="teams")                                               # Memberships in the Organiation

    class Meta:
        verbose_name = _("Team")
        verbose_name_plural = _("Teams")
        unique_together = ['name', 'organization']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse( "saasy:team-detail", kwargs={"slug": self.slug, "org_slug": self.organization.slug })

    def get_update_url(self):
        return reverse( "saasy:team-update", kwargs={"slug": self.slug, "org_slug": self.organization.slug })

    def get_delete_url(self):
        return reverse( "saasy:team-delete", kwargs={"slug": self.slug, "org_slug": self.organization.slug })
