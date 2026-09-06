from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    """
    Профиль сотрудника
    """
    user = models.OneToOneField(
            User,
            on_delete=models.CASCADE,
            related_name="employee_profile",
            verbose_name="Сотрудник",
            )
    full_name = models.CharField(
            "ФИО",
            max_length=255,
            )
    phone = models.CharField(
            "Телефон",
            max_length=50,
            blank=True,
            )
    address = models.TextField(
            "Адрес",
            blank=True,
            )
    position = models.CharField(
            "Должность",
            max_length=255,
            blank=True,
            )
    department = models.CharField(
            "Подразделение",
            max_length=255,
            blank=True
            )
    max_id = models.CharField(
            "Max ID",
            max_length=100,
            blank=True,
            help_text="ID пользователя в Max для отправки 2FA-кодов",
            )

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    def __str__(self) -> str:
        return self.full_name or str(self.user)
