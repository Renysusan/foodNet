from django.contrib import messages
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)

from django.urls import reverse
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.views import generic
from cuisines.models import Cuisine, CuisineMember
from . import models

class CreateNewCuisine(LoginRequiredMixin, generic.CreateView):
    fields = ("name", "description")
    model = Cuisine

class SingleCuisine(generic.DetailView):
    model = Cuisine

class ListCuisines(generic.ListView):
    model = Cuisine


class JoinCuisine(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("cuisines:single",kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        cuisine = get_object_or_404(Cuisine,slug=self.kwargs.get("slug"))

        try:
            CuisineMember.objects.create(user=self.request.user,cuisine=cuisine)

        except IntegrityError:
            messages.warning(self.request,("Warning, already a member of {}".format(cuisine.name)))

        else:
            messages.success(self.request,"You are now a member of the {} cuisine.".format(cuisine.name))

        return super().get(request, *args, **kwargs)


class LeaveCuisine(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("cuisines:single",kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):

        try:
            membership = models.CuisineMember.objects.filter(
                user=self.request.user,
                cuisine__slug=self.kwargs.get("slug")
            ).get()

        except models.CuisineMember.DoesNotExist:
            messages.warning(
                self.request,
                "You can't leave this cuisine because you aren't in it."
            )
        else:
            membership.delete()
            messages.success(
                self.request,
                "You have successfully left this cuisine."
            )
        return super().get(request, *args, **kwargs)
