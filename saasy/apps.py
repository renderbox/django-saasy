from django.conf import settings
from django.apps import AppConfig
from django.utils.module_loading import import_string

class SaasyConfig(AppConfig):
    name = 'saasy'
    prefix = "SAASY"
    __profile_model = None
    __organization_model = None

    def _setting(self, name, default=None):
        return getattr(settings, self.prefix + "_" + name, default)

    def set_model_setting(self, setting, default_model):
        attr = self._setting(setting)

        if not attr:
            attr = import_string(default_model)

        return attr

    @property
    def PROFILE_MODEL(self):
        """ User Profile for Saasy App """
        if not self.__profile_model:
            self.__profile_model = self.set_model_setting('PROFILE_MODEL', 'saasy.models.profile.Profile')
        return self.__profile_model

    @property
    def ORGANIZATION_MODEL(self):
        """ User Profile for Saasy App """
        if not self.__organization_model:
            self.__organization_model = self.set_model_setting('ORGANIZATION_MODEL', 'saasy.models.organization.Organization')
        return self.__organization_model
