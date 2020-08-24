from django.conf import settings
# from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.sites.models import Site

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
    fields = ['name']
    # form_class = OrganizationForm

    def form_valid(self, form):

        site = Site.objects.get_current()

        form.instance.site = site                 # Set the current Org site
        form.instance.owner = self.request.user.saasy_profile.get(site=site)     # Make the current user the Org owner

        return super().form_valid(form)


class OrganizationUpdateView(UpdateView):
    '''
    TODO: Need to block updating of a personal org.
    '''
    model = Organization
    fields = ['name']


class OrganizationDeleteView(DeleteView):
    model = Organization
