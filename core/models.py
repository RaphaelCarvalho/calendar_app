from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=100, verbose_name='Evento')
    description = models.TextField(blank=True, null=True, verbose_name='Descrição')
    date_event = models.DateTimeField(verbose_name='Data do evento')
    date_creation = models.DateTimeField(auto_now=True, verbose_name='Data da Criação')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'db_event'

    def __str__(self):
        return self.title

    def get_date_event(self):
        return self.date_event.strftime('%d/%m/%Y às %H:%M')