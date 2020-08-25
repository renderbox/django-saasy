from django.conf import settings
# from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.sites.models import Site
from django import forms

from saasy.models import Team, Organization


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

    def get_form(self, form_class=None):
        """Return an instance of the form to be used in this view."""
        form = super().get_form(form_class=form_class)

        if 'org' in self.request.GET:           # Set the initial value here
            form.fields['organization'].initial = Organization.on_site.get(slug=self.request.GET['org'])        # Prepopulate the value
            form.fields['organization'].widget = forms.HiddenInput()                                            # Hide it if known
        
        return form


class TeamUpdateView(UpdateView):
    '''
    TODO: Need to block updating of a personal org.
    '''
    model = Team
    fields = ['name']


class TeamDeleteView(DeleteView):
    model = Team
