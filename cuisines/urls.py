from django.conf.urls import url

from . import views

app_name = 'cuisines'

urlpatterns = [
    url(r"^$", views.ListCuisines.as_view(), name="all"),
    url(r"^new/$", views.CreateNewCuisine.as_view(), name="create"),
    url(r"^recipes/in/(?P<slug>[-\w]+)/$",views.SingleCuisine.as_view(),name="single"),
    url(r"join/(?P<slug>[-\w]+)/$",views.JoinCuisine.as_view(),name="join"),
    url(r"leave/(?P<slug>[-\w]+)/$",views.LeaveCuisine.as_view(),name="leave"),
]
