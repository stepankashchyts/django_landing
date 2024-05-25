from django.contrib import admin
from .models import Order,StatusCrm, CommentCrm

class Comment(admin.StackedInline):
    model = CommentCrm
    fields = ('comment_date', 'crm_comment')
    readonly_fields = ('comment_date',)
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','order_name', 'order_status','order_phone', 'order_date')
    list_display_links = ('id', 'order_name')
    list_editable = ('order_phone', 'order_status')
    list_filter = ('order_status',)
    list_per_page = 10
    list_max_show_all = 100
    fields = ('id','order_name', 'order_status','order_phone', 'order_date')
    readonly_fields = ('id', 'order_date')
    inlines = [Comment,]

# Register your models here.
admin.site.register(Order, OrderAdmin)
admin.site.register(StatusCrm)
admin.site.register(CommentCrm)
