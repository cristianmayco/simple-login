from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from . import forms
from . import models


class IndexView(TemplateView):
    template_name = 'index.html'


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = forms.RegisterUserForm
    success_url = ''

    class Meta:
        fields = ('email,')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('')

    def form_invalid(self, form):
        pass
