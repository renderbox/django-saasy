from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.sites.models import Site

from autoslug import AutoSlugField

# config = apps.get_app_config('saasy')

def set_user_profile_slug(instance):
    return instance.user.username


class SaasyProfile(models.Model):

    class Tier(models.IntegerChoices):
        FREE = 1, _('Free')
        PAID = 2, _('Paid')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("User"), on_delete=models.CASCADE, related_name="saasy_profile")
    slug = AutoSlugField(populate_from=set_user_profile_slug, unique=True, always_update=True)
    tier = models.IntegerField(choices=Tier.choices, default=Tier.FREE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, blank=True, null=True, related_name="saasy_profiles")

    class Meta:
        verbose_name = _("Saasy Profile")
        verbose_name_plural = _("Saasy Profiles")
        unique_together = ['site', 'user']

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse( "saasy:profile-detail", kwargs={"slug": self.slug})
