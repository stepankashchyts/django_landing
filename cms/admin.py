from django.contrib import admin
from .models import Cms_slider
from django.utils.safestring import mark_safe
# Register your models here.
class CmsAdmin(admin.ModelAdmin):
    list_display = ('cms_title','cms_text', 'cms_css', 'get_img')
    list_editable = ('cms_css',)
    list_display_links = ('cms_title',)
    fields = ('cms_title','cms_text', 'cms_css','cms_img', 'get_img')
    readonly_fields = ('get_img',)

    def get_img(self, obj):
        if obj.cms_img:
            return mark_safe(f'<img src ="{obj.cms_img.url}" width = 80px>')
        else: 
            return 'Image not found.'
    get_img.short_description = 'Image'



admin.site.register(Cms_slider, CmsAdmin)