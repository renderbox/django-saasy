from django.urls import path

from saasy import views

app_name = "saasy"

urlpatterns = [
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),

    path("orgs/", views.OrganizationListView.as_view(), name="organization-list"),
    path("orgs/add/", views.OrganizationCreateView.as_view(), name="organization-create"),
    path("org/<slug:slug>/", views.OrganizationDetailView.as_view(), name="organization-detail"),
    path("org/<slug:slug>/edit/", views.OrganizationUpdateView.as_view(), name="organization-update"),
    path("org/<slug:slug>/delete/", views.OrganizationDeleteView.as_view(), name="organization-delete"),

    path("projects/", views.ProjectListView.as_view(), name="project-list"),

    path("teams/", views.TeamListView.as_view(), name="team-list"),
]
