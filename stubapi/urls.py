from django.urls import path
from stubapi import views
from django.views.decorators.csrf import csrf_exempt


app_name = "stubapi"


urlpatterns = [
    path("sm1/", views.sm1),
    path("sm2/", views.sm2),
    path("facebook/", views.facebook),
    path("facebook/api/", csrf_exempt(views.facebook_api.as_view())),
]
