from django.urls import path

from saasy import views

app_name = "saasy"

urlpatterns = [
    path("", views.SaasyIndexView.as_view(), name="index"),
]
