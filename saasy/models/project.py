from django.conf import settings
from django.contrib.sites.models import Site
from django.db import models
from django.apps import apps
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from autoslug import AutoSlugField

class Project(models.Model):

    class Visibility(models.IntegerChoices):
        PUBLIC = 1, _('Public')
        PRIVATE = 2, _('Private')

    name = models.CharField(_("Name"), max_length=80, blank=True)
    slug = AutoSlugField(populate_from='name', unique=True, always_update=True)                                                                         # Gets set in the save
    organization = models.ForeignKey('saasy.Organization', verbose_name=_("Organization"), on_delete=models.CASCADE, related_name="projects")
    visibility = models.IntegerField(choices=Visibility.choices, default=Visibility.PUBLIC)

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse( "saasy:project-detail", kwargs={"slug": self.slug, "org_slug": self.organization.slug })

    def get_update_url(self):
        return reverse( "saasy:project-update", kwargs={"slug": self.slug, "org_slug": self.organization.slug })

    def get_delete_url(self):
        return reverse( "saasy:project-delete", kwargs={"slug": self.slug, "org_slug": self.organization.slug })
