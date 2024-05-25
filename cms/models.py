from django.db import models

# Create your models here.
class Cms_slider(models.Model):
    cms_img = models.ImageField(upload_to="slider_img/")
    cms_title = models.CharField(max_length=20, verbose_name="Title")
    cms_text = models.CharField(max_length=20, verbose_name="Text")
    cms_css = models.CharField(max_length=200, null=True, default="-", verbose_name="CSS Class")
    def __str__(self):
        return self.cms_title
    
    class Meta:
        verbose_name = "Slider"

