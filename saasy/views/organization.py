from django.conf import settings
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from saasy.models import Organization


class OrganizationListView(ListView):
    model = Organization

    def get_queryset(self):
        profile = self.request.user.saasy_profile.get(site=settings.SITE_ID)
        return super().get_queryset().filter(owner=profile)     # TODO: add filter to also include ones where the user is just a memeber of.

class OrganizationDetailView(DetailView):
    model = Organization


class OrganizationCreateView(CreateView):
    model = Organization
    fields = ['name', 'personal']


class OrganizationUpdateView(UpdateView):
    model = Organization


class OrganizationDeleteView(DeleteView):
    model = Organization
