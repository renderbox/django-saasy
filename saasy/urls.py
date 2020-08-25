from django.urls import path

from saasy import views

app_name = "saasy"

urlpatterns = [
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),

    path("orgs/", views.OrganizationListView.as_view(), name="organization-list"),
    path("orgs/add/", views.OrganizationCreateView.as_view(), name="organization-create"),
    path("org/<slug:slug>/", views.OrganizationDetailView.as_view(), name="organization-detail"),
    path("org/<slug:slug>/update/", views.OrganizationUpdateView.as_view(), name="organization-update"),
    path("org/<slug:slug>/delete/", views.OrganizationDeleteView.as_view(), name="organization-delete"),

    path("org/<slug:slug>/membership/", views.MembershipUpdateView.as_view(), name="membership-update"),

    path("projects/", views.ProjectListView.as_view(), name="project-list"),
    path("projects/add/", views.ProjectCreateView.as_view(), name="project-create"),
    path("orgs/<slug:org_slug>/<slug:slug>/", views.ProjectDetailView.as_view(), name="project-detail"),
    path("orgs/<slug:org_slug>/<slug:slug>/update/", views.ProjectUpdateView.as_view(), name="project-update"),
    path("orgs/<slug:org_slug>/<slug:slug>/delete/", views.ProjectDeleteView.as_view(), name="project-delete"),

    path("teams/", views.TeamListView.as_view(), name="team-list"),
    path("teams/add/", views.TeamCreateView.as_view(), name="team-create"),
    path("orgs/<slug:org_slug>/team/<slug:slug>/", views.TeamDetailView.as_view(), name="team-detail"),
    path("orgs/<slug:org_slug>/team/<slug:slug>/update/", views.TeamUpdateView.as_view(), name="team-update"),
    path("orgs/<slug:org_slug>/team/<slug:slug>/delete/", views.TeamDeleteView.as_view(), name="team-delete"),
]
