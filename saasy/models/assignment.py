import uuid

from django.conf import settings
from django.contrib.sites.models import Site
from django.db import models
from django.apps import apps
from django.utils.translation import gettext_lazy as _

from autoslug import AutoSlugField

from .choice import Roles


class Assignment(models.Model):
    """
    A Team's assignment on a given project.  It controls their permissions as a group.
    """

    uuid = models.UUIDField(_("UUID"), default=uuid.uuid4, editable=False, unique=True)
    team = models.ForeignKey('saasy.Team', verbose_name=_("Team"), on_delete=models.CASCADE, related_name="roles")
    project = models.ForeignKey('saasy.Project', verbose_name=_("Project"), on_delete=models.CASCADE, related_name="roles")
    role = models.IntegerField(_("Role"), choices=Roles.choices, default=Roles.USER)

    class Meta:
        verbose_name = _("Assignment")
        verbose_name_plural = _("Assignments")

    def __str__(self):
        return "{} @ {}".format(self.team.name, self.project.name)
