from django import forms
from .models import StudyClass


class ClassCreateForm(forms.ModelForm):
    class Meta:
        model = StudyClass
        fields = ["name", "subject", "age_group"]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-primary-500 focus:border-primary-500',
                'placeholder': 'Например: 10-А класс'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-primary-500 focus:border-primary-500',
                'placeholder': 'Например: Математика'
            }),
            'age_group': forms.NumberInput(attrs={
                'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-primary-500 focus:border-primary-500',
                'placeholder': 'Например: 16'
            }),
        }
        labels = {
            'name': 'Название класса',
            'subject': 'Предмет',
            'age_group': 'Средний возраст учеников',
        }
        