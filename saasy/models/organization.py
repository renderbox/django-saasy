import uuid

# from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
from django.urls import reverse

from autoslug import AutoSlugField


class Organization(models.Model):

    name = models.CharField(_("Name"), max_length=80)
    uuid = models.UUIDField(_("UUID"), default=uuid.uuid4, editable=False, unique=True)
    slug = AutoSlugField(populate_from='name', unique=True, always_update=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name="organizations")        # Overwriting this field from Base Class to change the related_name
    personal = models.BooleanField(default=False)
    owner = models.ForeignKey('saasy.SaasyProfile', verbose_name=_("Organization Owner"), on_delete=models.CASCADE, related_name="organizations")       # The top level person who controls the whole org

    objects = models.Manager()
    on_site = CurrentSiteManager()

    class Meta:
        verbose_name = _("Organization")
        verbose_name_plural = _("Organizations")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse( "saasy:organization-detail", kwargs={"slug": self.slug})

    def get_update_url(self):
        return reverse( "saasy:organization-update", kwargs={"slug": self.slug})

    def get_delete_url(self):
        return reverse( "saasy:organization-delete", kwargs={"slug": self.slug})

    def get_membership_url(self):
        return reverse( "saasy:membership-update", kwargs={"slug": self.slug})
