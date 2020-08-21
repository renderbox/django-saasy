from django.conf import settings as django_settings
from django.utils.module_loading import import_string


def set_model_setting(key, default):
    result = getattr(django_settings, key, default)

    print(result)


    if len(result.split(".")) > 2:
        result = import_string(result)
        print(result)

    return result

# For eventual customization of models
PROFILE_MODEL = set_model_setting("SAASY_PROFILE_MODEL", 'saasy.models.profile.SaasyProfile')
ORGANIZATION_MODEL = set_model_setting("SAASY_ORGANIZATION_MODEL", 'saasy.models.organization.Organization')
PROJECT_MODEL = set_model_setting("SAASY_PROJECT_MODEL", 'saasy.models.project.Project')



# from django.utils.module_loading import import_string

# class SaasyConfig():
#     __profile_model = None
#     __organization_model = None
#     __project_model = None

#     def _setting(self, name, default=None):
#         return getattr(settings, self.prefix + "_" + name, default)

#     def set_model_setting(self, setting, default_model):
#         attr = self._setting(setting)

#         if not attr:
#             attr = import_string(default_model)

#         return attr

#     @property
#     def PROFILE_MODEL(self):
#         """ User Profile for Saasy App """
#         if not self.__profile_model:
#             self.__profile_model = self.set_model_setting('PROFILE_MODEL', 'saasy.models.profile.SaasyProfile')
#         return self.__profile_model

#     @property
#     def ORGANIZATION_MODEL(self):
#         """ User Profile for Saasy App """
#         if not self.__organization_model:
#             self.__organization_model = self.set_model_setting('ORGANIZATION_MODEL', 'saasy.models.organization.Organization')
#         return self.__organization_model

#     @property
#     def PROJECT_MODEL(self):
#         """ User Profile for Saasy App """
#         if not self.__project_model:
#             self.__project_model = self.set_model_setting('PROJECT_MODEL', 'saasy.models.project.Project')
#         return self.__project_model
