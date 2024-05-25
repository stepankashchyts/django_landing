from django.db import models

# Create your models here.
class TeleSettings(models.Model):
    tg_token = models.CharField(max_length=50, verbose_name='Bot token')
    tg_chat = models.CharField(max_length=100, verbose_name='Chat ID')
    tg_message = models.TextField(verbose_name='Message')
    def __str__(self):
        return self.tg_message