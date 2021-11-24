import datetime

from django.db import models


class Task(models.Model):
    title = models.CharField('Заголовок поста', max_length=50)
    task = models.TextField('Текст поста')
    time = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ["time"]

    def get_absolute_url(self):
        return f'/{self.id}'

    def __str__(self):
        return self.title
