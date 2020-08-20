import uuid

from django.conf import settings
from django.contrib.sites.models import Site
from django.db import models
from django.apps import apps
from django.utils.translation import gettext_lazy as _

from autoslug import AutoSlugField

config = apps.get_app_config('saasy')

class TeamRole(models.Model):
    name = models.CharField(_("Name"), max_length=80, blank=True)
    uuid = models.UUIDField(_("UUID"), default=uuid.uuid4, editable=False, unique=True)
    slug = AutoSlugField(populate_from='name', unique=True, always_update=True)                                                                         # Gets set in the save

    def __str__(self):
        return self.name


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


class TeamAssignment(models.Model):
    """
    A Team's assignment on a given project.  It controls their permissions as a group.
    """

    uuid = models.UUIDField(_("UUID"), default=uuid.uuid4, editable=False, unique=True)
    team = models.ForeignKey(Team, verbose_name=_("Team"), on_delete=models.CASCADE, related_name="roles")
    project = models.ForeignKey(config.PROJECT_MODEL, verbose_name=_("Project"), on_delete=models.CASCADE, related_name="roles")
    roles = models.ManyToManyField(TeamRole, verbose_name=_("Roles"))

    class Meta:
        verbose_name = _("Team Assignment")
        verbose_name_plural = _("Team Assignments")

    def __str__(self):
        return "{} @ {}".format(self.team.name, self.project.name)
