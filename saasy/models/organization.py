import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.sites.models import Site
from django.apps import apps

from autoslug import AutoSlugField

from saasy import config

# config = apps.get_app_config('saasy')


class Organization(models.Model):

    name = models.CharField(_("Name"), max_length=80, blank=True)
    uuid = models.UUIDField(_("UUID"), default=uuid.uuid4, editable=False, unique=True)
    slug = AutoSlugField(populate_from='name', unique=True, always_update=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, blank=True, null=True, related_name="organizations")        # Overwriting this field from Base Class to change the related_name
    personal = models.BooleanField(default=False)
    owner = models.ForeignKey(config.PROFILE_MODEL, verbose_name=_("Organization Owner"), on_delete=models.CASCADE, related_name="organizations")       # The top level person who controls the whole org


    class Meta:
        verbose_name = _("Organization")
        verbose_name_plural = _("Organizations")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse( "organization-detail", kwargs={"slug": self.slug})
