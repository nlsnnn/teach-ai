from django import forms
from .models import LessonPlan
from classes.models import StudyClass


class LessonPlanCreateForm(forms.ModelForm):
    class Meta:
        model = LessonPlan
        fields = ["study_class", "topic", "hours", "preferences"]
        widgets = {
            'study_class': forms.Select(attrs={
                'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-primary-500 focus:border-primary-500'
            }),
            'topic': forms.TextInput(attrs={
                'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-primary-500 focus:border-primary-500',
                'placeholder': 'Например: Квадратные уравнения'
            }),
            'hours': forms.NumberInput(attrs={
                'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-primary-500 focus:border-primary-500',
                'min': 1,
                'max': 10
            }),
            'preferences': forms.Textarea(attrs={
                'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-primary-500 focus:border-primary-500',
                'placeholder': 'Например: включить групповую работу, использовать интерактивные материалы...',
                'rows': 4
            }),
        }
        labels = {
            'study_class': 'Класс',
            'topic': 'Тема урока',
            'hours': 'Количество часов',
            'preferences': 'Пожелания к плану',
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['study_class'].queryset = StudyClass.objects.filter(teacher=user)
        