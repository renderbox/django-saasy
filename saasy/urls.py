from django.urls import path

from saasy import views

urlpatterns = [
    path("", views.SaasyIndexView.as_view(), name="saasy-index"),
]
