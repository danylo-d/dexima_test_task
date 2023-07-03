from django.urls import path

from lead_gen.views import LeadGeneratorView

urlpatterns = [
    path("lead_generator/", LeadGeneratorView.as_view(), name="lead_generator"),
]


app_name = "lead_gen"
