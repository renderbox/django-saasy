from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from autoslug import AutoSlugField

# config = apps.get_app_config('saasy')

class Profile(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("User"), on_delete=models.CASCADE, related_name="saasy_profile")
    slug = AutoSlugField(populate_from='set_slug', unique=True, always_update=True)

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return "{} Profile".format(self.user.username)

    def set_slug(self, instance):
        return self.user.username

    def get_absolute_url(self):
        return reverse( "saasy:profile-detail", kwargs={"slug": self.slug})
