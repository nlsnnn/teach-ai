from django.urls import path
from . import views


urlpatterns = [
    path("", views.LessonPlanListView.as_view(), name="list"),
    path("create/", views.LessonPlanCreateView.as_view(), name="create"),
    path("<int:pk>/", views.LessonPlanDetailView.as_view(), name="detail"),
    path("<int:pk>/delete/", views.LessonPlanDeleteView.as_view(), name="delete"),
    path("<int:pk>/generate/", views.generate_ai_plan, name="generate"),
]
