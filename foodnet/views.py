from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

class LoginPage(TemplateView):
    template_name = 'login_redirect.html'

class LogoutPage(TemplateView):
    template_name = 'logout_redirect.html'

class HomePage(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("login_redirect"))
        return super().get(request, *args, **kwargs)