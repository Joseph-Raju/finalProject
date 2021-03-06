from django.urls import path
from stubapi import views
from django.views.decorators.csrf import csrf_exempt


app_name = "stubapi"


urlpatterns = [
    path("sm1/", views.sm1),
    path("sm2/", views.sm2),
    path("facebook/", views.facebook),
    path("twitter/", views.twitter),
    path("facebook/api/", views.facebook_api.as_view()),
    path("twitter/api/", views.twitter_api.as_view()),
    path("test1/", views.test1),
    path("test2/", views.test2),
    path("test3/", views.test3),
]
