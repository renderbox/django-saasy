import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from autoslug import AutoSlugField

# config = apps.get_app_config('saasy')


class Organization(models.Model):

    name = models.CharField(_("Name"), max_length=80, blank=True)
    uuid = models.UUIDField(_("UUID"), default=uuid.uuid4, editable=False, unique=True)
    slug = AutoSlugField(populate_from='name', unique=True, always_update=True)
    personal = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Organization")
        verbose_name_plural = _("Organizations")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse( "organization-detail", kwargs={"slug": self.slug})
