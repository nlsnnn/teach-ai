from django.db import models
from users.models import User


class StudyClass(models.Model):
    teacher = models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="Название класса")
    subject = models.CharField(max_length=200, verbose_name="Предмет")
    age_group = models.PositiveIntegerField(verbose_name="Средний возраст учеников")

    def __str__(self):
        return f"{self.name} ({self.subject})"


class LessonPlan(models.Model):
    topic = models.CharField(max_length=255, verbose_name="Тема урока")
    hours = models.PositiveIntegerField(default=1, verbose_name="Кол-во часов/уроков")
    preferences = models.TextField(null=True, blank=True, verbose_name="Пожелания")

    generated_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    pdf_file = models.FileField(upload_to="lesson_plans/pdf/", blank=True, null=True)
    docx_file = models.FileField(upload_to="lesson_plans/docx/", blank=True, null=True)

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="lesson_plans")
    study_class = models.ForeignKey(to=StudyClass, on_delete=models.CASCADE, related_name="lesson_plans")

    def __str__(self):
        return f"План: {self.topic} ({self.study_class})"
