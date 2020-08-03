from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from . import forms


class IndexView(TemplateView):
    template_name = 'index.html'


class LoginView(TemplateView):
    template_name = 'login.html'


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = forms.RegisterUserForm
    success_url = ''

    def form_valid(self, form):
        pass

    def form_invalid(self, form):
        pass
