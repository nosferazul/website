from django.contrib import admin
from .models import Customer,Product,Orders,Feedback,Checkreceipt
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'profile_pic')
    pass
admin.site.register(Customer, CustomerAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'product_image')
admin.site.register(Product, ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    pass
admin.site.register(Orders, OrderAdmin)

class FeedbackAdmin(admin.ModelAdmin):
    pass
admin.site.register(Feedback, FeedbackAdmin)
# Register your models here.

class CheckreceiptAdmin(admin.ModelAdmin):
    pass
admin.site.register(Checkreceipt, CheckreceiptAdmin)

