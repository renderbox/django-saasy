from django.conf import settings
# from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.sites.models import Site

from saasy.models import Membership
# from saasy.models import Organization


class MembershipUpdateView(ListView):
    '''
    TODO: Need to block updating of a personal org.
    '''
    model = Membership

    # template_name = "saasy/membership_detail.html"
    # fields = ['name']

    # Get all the members of an Org
    # Get all the members of the site to be added.

    def get_queryset(self):
        # org = Organization.objects.get(slug=self.kwargs['slug'])
        queryset = super().get_queryset().filter(organization__slug=self.kwargs['slug'])
        return queryset

    # def get_context

# class MembershipDeleteView(DeleteView):
#     model = Membership
