import uuid

from django.conf import settings
from django.contrib.sites.models import Site
from django.db import models
from django.apps import apps
from django.utils.translation import gettext_lazy as _

from autoslug import AutoSlugField

from saasy import config

# config = apps.get_app_config('saasy')

class Role(models.Model):
    name = models.CharField(_("Name"), max_length=80, blank=True)
    uuid = models.UUIDField(_("UUID"), default=uuid.uuid4, editable=False, unique=True)
    slug = AutoSlugField(populate_from='name', unique=True, always_update=True)                                                                         # Gets set in the save

    def __str__(self):
        return self.name