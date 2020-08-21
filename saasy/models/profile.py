from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
from django.urls import reverse
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

from autoslug import AutoSlugField

def set_user_username_as_slug(instance):
    return instance.user.username


class SaasyProfile(models.Model):

    class Tier(models.IntegerChoices):
        FREE = 1, _('Free')
        PAID = 2, _('Paid')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("User"), on_delete=models.CASCADE, related_name="saasy_profile")
    slug = AutoSlugField(populate_from=set_user_username_as_slug, unique=True, always_update=True)
    tier = models.IntegerField(choices=Tier.choices, default=Tier.FREE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, blank=True, null=True, related_name="saasy_profiles")

    objects = models.Manager()
    on_site = CurrentSiteManager()

    class Meta:
        verbose_name = _("Saasy Profile")
        verbose_name_plural = _("Saasy Profiles")
        unique_together = ['site', 'user']

    def __str__(self):
        return self.user.username

    # def get_absolute_url(self):
    #     return reverse( "saasy:profile-detail", kwargs={"slug": self.slug})


def create_user_profile(sender, instance, created, **kwargs):
    '''
    Adds a SaasyProfile if User does not have one
    '''

    if created:
        profile, created = SaasyProfile.objects.get_or_create(site=Site.objects.get_current(), user=instance)       # Using this aproach to add the site requires it be set inside of the settings.py
        if created:
            profile.save()

post_save.connect(create_user_profile, sender=get_user_model(), dispatch_uid="create_user_profile")
