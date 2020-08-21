from django.views.generic import TemplateView

from saasy.models import SaasyProfile, Organization, Project

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_count']  = SaasyProfile.on_site.all().count()
        context['project_count'] = Project.objects.all().count()
        context['organization_count'] = Organization.on_site.all().count()
        return context
