from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from .forms import LeadGeneratorForm


class LeadGeneratorView(LoginRequiredMixin, TemplateView):
    template_name = "lead_gen/lead_gen.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = LeadGeneratorForm()
        return context

    def post(self, request, *args, **kwargs):
        form = LeadGeneratorForm(request.POST)
        if form.is_valid():
            keywords = form.cleaned_data["keywords"]
            location = form.cleaned_data["location"]
            lead_count = form.cleaned_data["lead_count"]

            # Implementation of the lead generator, with data from the form
