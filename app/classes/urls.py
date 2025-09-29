from django.urls import path
from . import views


urlpatterns = [
    path("", views.ClassListView.as_view(), name="list"),
    path("create/", views.ClassCreateView.as_view(), name="create"),
    path("<int:pk>/", views.ClassDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", views.ClassUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", views.ClassDeleteView.as_view(), name="delete"),
]
