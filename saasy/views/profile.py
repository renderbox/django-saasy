from django.conf import settings
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from saasy.models import SaasyProfile


class ProfileDetailView(DetailView):
    model = SaasyProfile

