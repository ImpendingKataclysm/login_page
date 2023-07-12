from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django import forms

from password import Password


class HomePage(TemplateView):
    template_name = 'home.html'


class SignUpPage(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            password = Password().generate()
            return JsonResponse({'password': password})
        return super().get(request, *args, **kwargs)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['generate_password'] = self.request.POST.get('generate_password')
    #     return context


def generate_password(request):
    if request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest" and request.method == 'GET':
        password = Password().generate()
        return JsonResponse({'password': password})
    return JsonResponse({}, status=400)
