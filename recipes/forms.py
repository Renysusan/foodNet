from django import forms
from recipes import models


class RecipeForm(forms.ModelForm):
    class Meta:
        fields = ("dish_title", "dish_image", "cooking_time", "method", "cuisine")
        model = models.Recipe

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields["cuisine"].queryset = (
                models.Cuisine.objects.filter(
                    pk__in=user.cuisines.values_list("cuisine__pk")
                )
            )
