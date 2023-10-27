from django.db import models

# Create your models here.
class Plan(models.Model):
    title = models.CharField(max_length=30, verbose_name="Название программы")
    price = models.FloatField(null=True, blank=True, verbose_name="Цена")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Тарифы'
        verbose_name = 'Тариф'

class Program(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название тарифа")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Программы'
        verbose_name = 'Программа'

class Client(models.Model):
    first_name = models.CharField(max_length=20, verbose_name="Имя")
    last_name = models.CharField(max_length=20, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=20, verbose_name="Отчество", null=True, blank=True)
    birth_date = models.DateField(db_index=True, verbose_name="Дата рождения")

    def __str__(self):
        return f"{self.last_name} {self.name}"

    class Meta:
        verbose_name_plural = 'Клиенты'
        verbose_name = 'Клиент'

class PlanProgram(models.Model):
    plan = models.ForeignKey("Plan", on_delete=models.CASCADE, verbose_name="Тариф")
    program = models.ForeignKey("Program", on_delete=models.CASCADE, verbose_name="Программа")

    # def __str__(self):
    #     return f"Тариф: {self.plan.title}, Програма: {self.program.name}"

    class Meta:
        verbose_name_plural = 'Составы тарифов'
        verbose_name = 'Состав тарифа'

class Subscription(models.Model):
    client = models.ForeignKey("Client", on_delete=models.CASCADE, verbose_name="Клиент")
    plan = models.ForeignKey("Plan", on_delete=models.DO_NOTHING, verbose_name="Тариф")
    date_start = models.DateField(verbose_name="Дата начала")
    date_end = models.DateField(verbose_name="Дата окончания")