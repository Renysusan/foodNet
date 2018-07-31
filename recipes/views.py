from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from .models import Recipe
from django.urls import reverse_lazy
from django.http import Http404
from django.views import generic

from braces.views import SelectRelatedMixin

from . import forms
from . import models

from django.contrib.auth import get_user_model
User = get_user_model()


class RecipeList(SelectRelatedMixin, generic.ListView):
    model = models.Recipe
    select_related = ("user", "cuisine")


class UserRecipes(generic.ListView):
    model = models.Recipe
    template_name = "recipes/user_recipe_list.html"

    def get_queryset(self):
        try:
            self.recipe_user = User.objects.prefetch_related("recipes").get(
                username__iexact=self.kwargs.get("username")
            )
        except User.DoesNotExist:
            raise Http404
        else:
            return self.recipe_user.recipes.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recipe_user"] = self.recipe_user
        return context


class RecipeDetail(SelectRelatedMixin, generic.DetailView):
    model = models.Recipe
    select_related = ("user", "cuisine")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            user__username__iexact=self.kwargs.get("username")
        )

class CreateRecipe(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    fields = ('dish_title', 'dish_image', 'cooking_time', 'method', 'cuisine')
    model = models.Recipe

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user 
        self.object.save()
        return super().form_valid(form)

class UpdateRecipe(LoginRequiredMixin, SelectRelatedMixin, generic.UpdateView):
    fields = ('dish_title', 'dish_image', 'cooking_time', 'method')
    model = models.Recipe
    select_related = ("user", "cuisine")
    template_name = "recipes/recipe_update_form.html"

class DeleteRecipe(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.Recipe
    select_related = ("user", "cuisine")
    success_url = reverse_lazy("recipes:all")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Recipe Deleted")
        return super().delete(*args, **kwargs)

def UpvoteRecipe(request, pk):
    if request.method == 'POST':
        recipe = get_object_or_404(Recipe, pk=pk)
        recipe.votes_total += 1
        recipe.save()
        return redirect('/recipes/by/' +  str(request.user.username) + '/' + str(pk))



