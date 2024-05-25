from django.db import models
from django import forms

# Create your models here.
class StatusCrm(models.Model):
    status = models.CharField(max_length=20, verbose_name='Status')
    def __str__(self):
        return self.status
    
class Order(models.Model):
    order_name = models.CharField(max_length=150, verbose_name='Name')
    order_date=models.DateTimeField(auto_now=True, verbose_name='Created at')
    order_phone=models.CharField(max_length=150, verbose_name='Phone Number')
    order_status = models.ForeignKey(StatusCrm,  on_delete=models.PROTECT, null=True, blank=True, verbose_name='CRM Status`')
    def __str__(self):
        return self.order_name


class CommentCrm(models.Model):
    comment_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='binding')
    crm_comment = models.TextField(verbose_name='CRM Comment')
    comment_date = models.DateTimeField(auto_now=True, verbose_name='Created at')
    def __str__(self):
        return self.crm_comment