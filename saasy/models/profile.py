from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from autoslug import AutoSlugField

# config = apps.get_app_config('saasy')

def set_user_profile_slug(instance):
    return instance.user.username


class Profile(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("User"), on_delete=models.CASCADE, related_name="saasy_profile")
    slug = AutoSlugField(populate_from=set_user_profile_slug, unique=True, always_update=True)

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse( "saasy:profile-detail", kwargs={"slug": self.slug})
