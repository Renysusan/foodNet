from django.conf.urls import url
from . import views

app_name='recipes'

urlpatterns = [
    url(r"^$", views.RecipeList.as_view(), name="all"),
    url(r"new/$", views.CreateRecipe.as_view(), name="create"),
    url(r"by/(?P<username>[-\w]+)/$",views.UserRecipes.as_view(),name="for_user"),
    url(r"by/(?P<username>[-\w]+)/(?P<pk>\d+)/$",views.RecipeDetail.as_view(),name="single"),
    url(r"delete/(?P<pk>\d+)/$",views.DeleteRecipe.as_view(),name="delete"),
    url(r"upvote/(?P<pk>\d+)/$",views.UpvoteRecipe,name="upvote"),
    url(r"update/(?P<pk>\d+)/$",views.UpdateRecipe.as_view(),name="update"),
]