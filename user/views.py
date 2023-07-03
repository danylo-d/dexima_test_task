from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import UserRegistrationForm
from .models import User


class UserRegistrationView(CreateView):
    model = User
    template_name = "registration/register.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("login")
