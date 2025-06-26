from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    # ex: /polls/
    path("", views.IndexView.as_view(), name="index"), # Changed from views.index
    # ex: /polls/5/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"), # Changed from views.detail
    # ex: /polls/5/results/
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"), # Changed from views.results
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]