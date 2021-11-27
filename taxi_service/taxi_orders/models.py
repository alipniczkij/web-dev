from django.db import models


class Machine(models.Model):
    class Meta:
        verbose_name_plural = 'Машины'
        verbose_name = 'Машина'
        ordering = ['-release_year']
    brand = models.CharField(max_length=50, verbose_name='Марка')
    level = models.CharField(max_length=50, verbose_name='Класс')
    numbers = models.CharField(max_length=50, verbose_name='Номера')
    color = models.CharField(max_length=50, verbose_name='Цвет')
    release_year = models.DateField(verbose_name='Дата выпуска', db_index=True)

    def __str__(self):
        return self.color + ' ' + self.brand + ' ' + self.numbers


class Driver(models.Model):
    class Meta:
        verbose_name_plural = 'Водители'
        verbose_name = 'Водитель'
        ordering = ['surname']
    machine = models.ForeignKey(Machine, on_delete=models.DO_NOTHING, verbose_name='Машина')
    name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия', db_index=True)
    patronymic = models.CharField(max_length=50, verbose_name='Отчество')
    birthday = models.DateField(verbose_name='День рождения')
    inn = models.CharField(max_length=50, verbose_name='ИНН')
    passport = models.CharField(max_length=50, verbose_name='Паспорт')

    def __str__(self):
        return self.name + ' ' + self.surname


class Order(models.Model):
    class Meta:
        verbose_name_plural = 'Заказы'
        verbose_name = 'Заказ'
        ordering = ['-created_at']
    driver = models.ForeignKey(Driver, on_delete=models.DO_NOTHING, verbose_name='Водитель')
    passengers_num = models.IntegerField(blank=True, verbose_name='Количество пассажиров')
    route_length = models.FloatField(verbose_name='Длина пути (километры)')  # kilometers
    address_from = models.CharField(max_length=100, verbose_name='Точка подачи')
    address_to = models.CharField(max_length=100, verbose_name='Точка назначения')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания', db_index=True)
