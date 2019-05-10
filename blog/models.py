from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


''' мой класс для сущности Spend - расход средств
    поля:
         category       - категория траты
         name           - наименование расхода
         created_date   - дата и время создания
         amount         - сумма расхода
'''
class Spend(models.Model):
    # поля модели
    category = models.CharField(max_length=100, help_text='Категория')
    name = models.CharField(max_length=200, help_text='Наименование расхода')
    created_date = models.DateTimeField(default=timezone.now)
    amount = models.FloatField(help_text='Сумма', default=0.0)

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __unicode__(self):
        return 'Операция: %s Категория: %s' % (self.name, self.category)

    def __str__(self):
        return self.name

