from django.db import models

# Create your models here.
class PriceCard(models.Model):
    pc_value = models.CharField(max_length=20, verbose_name="Price")
    pc_description = models.CharField(max_length= 100, verbose_name="Description")
    pc_title = models.CharField(max_length= 100, verbose_name="Title", null=True, default="жалупа")
    def __str__(self):
        return self.pc_value


class PriceTable(models.Model):
    pt_title= models.CharField(max_length=20, verbose_name="Title")
    pt_old_price = models.CharField(max_length=20, verbose_name="Old Price")
    pt_new_price = models.CharField(max_length=20, verbose_name="New Price")
    def __str__(self):
        return self.pt_title