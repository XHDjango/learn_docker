from django.urls import path

from . import views

# 为 URL 名称添加命名空间，以分辨重名的 URL
app_name = "polls"

urlpatterns = [
    path("", views.index, name="index"),  # ex: /polls/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),  # ex: /polls/5/
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),  # ex: /polls/5/results/
    path("<int:question_id>/vote/", views.vote, name="vote"),  # ex: /polls/5/vote/
]
