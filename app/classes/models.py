from django.db import models
from users.models import User


class StudyClass(models.Model):
    teacher = models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="Название класса")
    subject = models.CharField(max_length=200, verbose_name="Предмет")
    age_group = models.PositiveIntegerField(verbose_name="Средний возраст учеников")

    def __str__(self):
        return f"{self.name} ({self.subject})"
    