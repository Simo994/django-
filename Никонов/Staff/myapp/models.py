from django.db import models

class Task(models.Model):
    name = models.CharField('Название товара', max_length=100)
    place = models.CharField('Имя сотрудника', max_length=100, )
    price = models.IntegerField('Цена')
    square = models.IntegerField('Время продажи')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продавец'
        verbose_name_plural = 'Продавцы'