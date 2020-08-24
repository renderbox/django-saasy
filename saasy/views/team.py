from django.conf import settings
# from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.sites.models import Site

from saasy.models import Team


class TeamListView(ListView):
    model = Team

    # def get_queryset(self):
    #     profile = self.request.user.saasy_profile.get(site=settings.SITE_ID)
    #     return super().get_queryset().filter(owner=profile)     # TODO: add filter to also include ones where the user is just a memeber of.

class TeamDetailView(DetailView):
    model = Team


class TeamCreateView(CreateView):
    model = Team
    fields = ['name', 'organization']
    # form_class = TeamForm

    # TODO: Filter organizations to where the user is the owner
    # TODO: Expand Filter of Organiztions to ones where the user is Member with Admin Privilages

    # TODO: If 'org' is passed in, set the default to the relevent org

    def get_initial(self):
        initial = super().get_initial()

        return initial

    # def form_valid(self, form):

    #     site = Site.objects.get_current()

    #     form.instance.site = site                 # Set the current Org site
    #     form.instance.owner = self.request.user.saasy_profile.get(site=site)     # Make the current user the Org owner

    #     return super().form_valid(form)


class TeamUpdateView(UpdateView):
    '''
    TODO: Need to block updating of a personal org.
    '''
    model = Team
    fields = ['name']


class TeamDeleteView(DeleteView):
    model = Team
