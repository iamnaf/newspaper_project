from django.shortcuts import render
from django.urls import reverse_lazy
from django.urls.base import reverse
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

# Create your views here.

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'