from django.contrib.auth import get_user_model
from django.db import models


class Order(models.Model):
    class ChoicesStatus(models.TextChoices):
        NEW = 'Новая', "Новая"
        ACCEPT = 'Принято в работу', 'Принято в работу'
        DONE = 'Выполнено', 'Выполнено'

    class ChoicesDesign(models.TextChoices):
        for_children = 'Для детей', "Для детей"
        for_teenagers = 'Для подростков', 'Для подростков'
        for_students = 'Для студентов', 'Для студентов'
        for_adults = 'Для взрослых', 'Для взрослых'
        for_pensioners = 'Для пенсионеров', 'Для пенсионеров'

    title = models.CharField(max_length=100,verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    status = models.CharField(max_length=50, choices=ChoicesStatus.choices, default=ChoicesStatus.NEW, verbose_name='Статус заказа')
    photo = models.ImageField('Изображение категории', upload_to='image/', default=None, null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='orders')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    category = models.CharField(max_length=50, choices=ChoicesDesign.choices,verbose_name='Категория книг',default=ChoicesDesign.for_children)

    objects = models.Manager()

    def __str__(self):
        return self.user.username  # type: ignore

    class Meta:
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказы'
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]

