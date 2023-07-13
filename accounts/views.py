from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from password import Password


class HomePage(TemplateView):
    template_name = 'home.html'


class SignUpPage(CreateView):
    """
    Registration form for new users
    """
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def get(self, request, *args, **kwargs):
        """
        Generates a secure password upon user request
        :param request: User's request for a new secure password
        :param args: default from CreateView
        :param kwargs: default from CreateView
        :return: The secure password requested by the user
        """
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            password = Password().generate()
            return JsonResponse({'password': password})
        return super().get(request, *args, **kwargs)
