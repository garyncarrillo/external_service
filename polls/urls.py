from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    # /polls/:question_id
    path("<int:question_id>/", views.details, name = "details"),
    # /polls/:question_id/results
    path("<int:question_id>/results/", views.results, name = "results"),
    # /polls/:question_id/vote
    path("<int:question_id>/vote/", views.vote, name = "vote"),
]