from django.db import models
from django.utils.translation import gettext_lazy as _

class Roles(models.IntegerChoices):
    USER = 1, _("user")
    STAFF = 5, _("staff")
    ADMIN = 10, _("admin")
    