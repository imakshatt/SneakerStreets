from django.contrib import admin
from .models import LOGIN_TABLE, SHOES_TABLE, BRAND_TABLE, CATEGORY_TABLE, CART_TABLE, ORDER_TABLE, STOCK_TABLE, CONTACT_TABLE, FEEDBACK
# Register your models here.

class LoginDetailDisplay(admin.ModelAdmin):
    list_display = ("EMAIL_ID","PHONE_NO","user_photo","ROLE","STATUS","NAME","DOB","ADDRESS")
    search_fields = ['NAME', 'PHONE_NO','EMAIL_ID']
    list_filter = ['STATUS']

admin.site.register(LOGIN_TABLE, LoginDetailDisplay)

admin.site.register(BRAND_TABLE)
admin.site.register(CATEGORY_TABLE)

class ShoesTableDisplay(admin.ModelAdmin):
    list_display = ("BRAND_ID","NAME","PRICE","CATEGORY_ID","SIZE","COLOR","TYPE","shoe_photo")

admin.site.register(SHOES_TABLE, ShoesTableDisplay)

class CartTableDisplay(admin.ModelAdmin):
    list_display = ("SHOES_ID","BRAND_ID","L_ID","SHOES_NAME","CATEGORY_ID","DATE","QUANTITY","PRICE","FINAL_PRICE","ORDER_ID","ORDER_STATUS") #

admin.site.register(CART_TABLE, CartTableDisplay)

class OrderTableDisplay(admin.ModelAdmin):
    list_display = ("TOTAL_AMOUNT","L_ID", "ADDRESS", "DATETIME","PAYMENT_STATUS","ORDER_STATUS")

admin.site.register(ORDER_TABLE, OrderTableDisplay)


class StockTableDisplay(admin.ModelAdmin):
    list_display = ("BRAND_ID","CATEGORY_ID","SHOES_ID","COMMENT")

admin.site.register(STOCK_TABLE, StockTableDisplay)

class ContactTableDisplay(admin.ModelAdmin):
    list_display = ("MESSAGE","EMAIL_ID","FULL_NAME","PHONE_NO")

admin.site.register(CONTACT_TABLE, ContactTableDisplay)

class FeedbackDisplay(admin.ModelAdmin):
    list_display = ("L_ID","RATINGS","COMMENT")

admin.site.register(FEEDBACK, FeedbackDisplay)

