from django.contrib import admin
from . models import Cart, OrderPlaced, Payment, Product,Customer
# Register your models here.
@admin.register(Product)
class productModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','discounted_price','product_image']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','locality','city','state','zipcode']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']

@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','amount','razorpay_order_id','razorpay_payment_status','razorpay_payment_id','paid'] 

@admin.register(OrderPlaced)  
class OrderPlacedModelAdmin(admin.ModelAdmin):
    ['id','user','customer','quantity','ordered_date','status','payment']  
