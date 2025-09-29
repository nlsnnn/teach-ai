from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

from .models import LessonPlan
from .forms import LessonPlanCreateForm
from .ai import IOAi
from .schemas import AIPlanRequest


class LessonPlanListView(LoginRequiredMixin, ListView):
    model = LessonPlan
    context_object_name = "plans"
    template_name = "lesson_plans/list.html"
    
    def get_queryset(self):
        return LessonPlan.objects.filter(user=self.request.user).select_related('study_class')


class LessonPlanCreateView(LoginRequiredMixin, CreateView):
    model = LessonPlan
    form_class = LessonPlanCreateForm
    template_name = "lesson_plans/create.html"
    success_url = reverse_lazy("lessons:list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class LessonPlanDetailView(LoginRequiredMixin, DetailView):
    model = LessonPlan
    template_name = "lesson_plans/detail.html"
    context_object_name = "plan"
    
    def get_queryset(self):
        return LessonPlan.objects.filter(user=self.request.user)


class LessonPlanDeleteView(LoginRequiredMixin, DeleteView):
    model = LessonPlan
    template_name = "lesson_plans/delete.html"
    success_url = reverse_lazy("lessons:list")
    
    def get_queryset(self):
        return LessonPlan.objects.filter(user=self.request.user)


@require_http_methods(["POST"])
@login_required()
def generate_ai_plan(request, pk):
    # if not request.user.is_authenticated:
    #     return JsonResponse({'error': 'Требуется авторизация'}, status=401)
    
    plan = get_object_or_404(LessonPlan, pk=pk, user=request.user)
    
    try:
        ai_client = IOAi()
        
        ai_request = AIPlanRequest(
            class_name=plan.study_class.name,
            subject=plan.study_class.subject,
            age=plan.study_class.age_group,
            topic=plan.topic,
            hours=plan.hours,
            preferences=plan.preferences or None
        )
        
        generated_text = ai_client.get_ai_plan(ai_request)
        plan.generated_text = generated_text
        plan.save()
        
        return JsonResponse({
            'success': True,
            'generated_text': generated_text
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)
