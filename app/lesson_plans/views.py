from django.shortcuts import render
from django.views.generic import ListView
from .models import LessonPlan


class PlansListView(ListView):
    model = LessonPlan
    context_object_name = "plans"