from django.conf import settings
from django.views.generic import TemplateView

from saasy.models import SaasyProfile

from .team import TeamListView, TeamDetailView, TeamCreateView, TeamUpdateView, TeamDeleteView
from .organization import OrganizationListView, OrganizationDetailView, OrganizationCreateView, OrganizationUpdateView, OrganizationDeleteView
from .project import ProjectListView, ProjectDetailView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView
from .profile import ProfileDetailView
from .membership import MembershipUpdateView

from saasy.models import Organization, Project, Team

class DashboardView(TemplateView):
    template_name = "saasy/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.request.user.saasy_profile.get(site=settings.SITE_ID)
        context['organizations'] = Organization.on_site.filter(owner=profile)[:3]
        context['projects'] = Project.objects.all()[:3]         # TODO: Filter on the current user's Organizations
        context['teams'] = Team.objects.all()[:3]               # TODO: Filter on the current user Memberships
        return context
