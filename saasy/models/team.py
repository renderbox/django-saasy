from django.conf import settings
from django.contrib.sites.models import Site
from django.db import models
from django.apps import apps
from django.utils.translation import gettext_lazy as _

from autoslug import AutoSlugField

config = apps.get_app_config('saasy')

class Team(models.Model):

    name = models.CharField(_("Name"), max_length=80, blank=True)
    slug = AutoSlugField(populate_from='name', unique=True, always_update=True)                                                                         # Gets set in the save
    organization = models.ForeignKey(config.ORGANIZATION_MODEL, verbose_name=_("Organization"), on_delete=models.CASCADE, related_name="teams")
    members = models.ManyToManyField('saasy.Membership', verbose_name=_("Members"), related_name="teams")

    class Meta:
        verbose_name = _("Team")
        verbose_name_plural = _("Teams")
        unique_together = ['name', 'organization']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse( "team-detail", kwargs={"org": self.organization.slug, "slug": self.slug})


class TeamRole(models.Model):

    class TeamRoleType(models.IntegerChoices):
        ADMIN = 10, _("Administrator")
        USER = 1, _("User")

    name = models.CharField(_("Name"), max_length=80, blank=True)
    uuid = models.UUIDField(_("UUID"))
    team = models.ForeignKey(Team, verbose_name=_("Team"), on_delete=models.CASCADE, related_name="roles")
    project = models.ForeignKey(config.ORGANIZATION_MODEL, verbose_name=_("Project"), on_delete=models.CASCADE, related_name="roles")
    role_type = models.IntegerField(_("Role Type"), choices=TeamRoleType.choices, default=TeamRoleType.USER)

    class Meta:
        verbose_name = _("Team Role")
        verbose_name_plural = _("Team Roles")

    def __str__(self):
        return self.name
