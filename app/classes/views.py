from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import StudyClass
from .forms import ClassCreateForm


class ClassListView(LoginRequiredMixin, ListView):
    model = StudyClass
    context_object_name = "classes"
    template_name = "classes/list.html"
    
    def get_queryset(self):
        return StudyClass.objects.filter(teacher=self.request.user)


class ClassCreateView(LoginRequiredMixin, CreateView):
    form_class = ClassCreateForm
    template_name = "classes/create.html"
    success_url = reverse_lazy("classes:list")
    
    def form_valid(self, form):
        form.instance.teacher = self.request.user
        return super().form_valid(form)


class ClassUpdateView(LoginRequiredMixin, UpdateView):
    model = StudyClass
    form_class = ClassCreateForm
    template_name = "classes/create.html"
    success_url = reverse_lazy("classes:list")
    
    def get_queryset(self):
        return StudyClass.objects.filter(teacher=self.request.user)


class ClassDeleteView(LoginRequiredMixin, DeleteView):
    model = StudyClass
    template_name = "classes/delete.html"
    success_url = reverse_lazy("classes:list")
    
    def get_queryset(self):
        return StudyClass.objects.filter(teacher=self.request.user)


class ClassDetailView(LoginRequiredMixin, DetailView):
    model = StudyClass
    template_name = "classes/detail.html"
    context_object_name = "study_class"
    
    def get_queryset(self):
        return StudyClass.objects.filter(teacher=self.request.user)
    
