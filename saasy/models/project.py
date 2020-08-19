from django.conf import settings
from django.contrib.sites.models import Site
from django.db import models
from django.apps import apps
from django.utils.translation import gettext_lazy as _

from autoslug import AutoSlugField

config = apps.get_app_config('saasy')

class Project(models.Model):

    name = models.CharField(_("Name"), max_length=80, blank=True)
    slug = AutoSlugField(populate_from='name', unique=True, always_update=True)                                                                         # Gets set in the save
    organization = models.ForeignKey(config.ORGANIZATION_MODEL, verbose_name=_("Organization"), on_delete=models.CASCADE, related_name="projects")

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

    def __str__(self):
        return self.name

#     def get_absolute_url(self):
#         return reverse( "samplemodel_detail", kwargs={"slug": self.slug})
