from django.db import models
from django.utils.safestring import mark_safe
# Create your models here.

class LOGIN_TABLE(models.Model):
    choice = ((0, 'Active'),
            (1, 'Inactive'))
    role_choice = ((0, 'ADMIN'),
              (1, 'USER'))

    EMAIL_ID = models.EmailField()
    PHONE_NO = models.IntegerField()
    PASSWORD = models.CharField(max_length=300)
    DP = models.ImageField(upload_to='photos')
    ROLE = models.IntegerField(choices=role_choice)
    STATUS = models.IntegerField(choices=choice)
    NAME = models.CharField(max_length=300)
    DOB = models.DateTimeField()
    ADDRESS = models.CharField(max_length=500)

    def user_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.DP.url))

    user_photo.allow_tags = True

    def __str__(self):
        return self.NAME

class BRAND_TABLE(models.Model):
    BRAND_NAME = models.CharField(max_length=300)

    def __str__(self):
        return self.BRAND_NAME

class CATEGORY_TABLE(models.Model):
    CATEGORY_NAME = models.CharField(max_length=300)

    def __str__(self):
        return self.CATEGORY_NAME

class SHOES_TABLE(models.Model):
    BRAND_ID = models.ForeignKey(BRAND_TABLE, on_delete=models.CASCADE,default="")
    CATEGORY_ID = models.ForeignKey(CATEGORY_TABLE, on_delete=models.CASCADE,default="")
    SIZE = models.IntegerField()
    PRICE = models.IntegerField(default=100)
    COLOR = models.CharField(max_length=300)
    TYPE = models.CharField(max_length=300)
    NAME = models.CharField(max_length=300)
    SHOE_PHOTO = models.ImageField(upload_to='photos')

    def shoe_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.SHOE_PHOTO.url))

    shoe_photo.allow_tags = True

    def __str__(self):
        return self.NAME

class CART_TABLE(models.Model):
    SHOES_ID = models.ForeignKey(SHOES_TABLE, on_delete=models.CASCADE,default="")
    BRAND_ID = models.ForeignKey(BRAND_TABLE, on_delete=models.CASCADE,default="")
    L_ID = models.ForeignKey(LOGIN_TABLE, on_delete=models.CASCADE,default="")
    CATEGORY_ID = models.ForeignKey(CATEGORY_TABLE, on_delete=models.CASCADE,default="")
    SHOES_NAME = models.CharField(max_length=300)
    DATE = models.DateTimeField(auto_now=True, editable=False)
    PRICE = models.IntegerField(default=100)
    QUANTITY = models.IntegerField()
    FINAL_PRICE = models.IntegerField(default=160)
    ORDER_ID = models.IntegerField(default=0)
    ORDER_STATUS = models.IntegerField(default=0)


    def __str__(self):
        return self.SHOES_NAME + " Cart"

class ORDER_TABLE(models.Model):
    TOTAL_AMOUNT = models.IntegerField(default=0)
    L_ID = models.ForeignKey(LOGIN_TABLE, on_delete=models.CASCADE, default="")
    ADDRESS = models.CharField(max_length=500)
    DATETIME = models.DateTimeField(auto_now=True, editable=False)
    PAYMENT_STATUS = models.CharField(max_length=300,default="")
    ORDER_STATUS = models.CharField(max_length=300,default="")


class STOCK_TABLE(models.Model):
    BRAND_ID = models.ForeignKey(BRAND_TABLE, on_delete=models.CASCADE,default="")
    CATEGORY_ID = models.ForeignKey(CATEGORY_TABLE, on_delete=models.CASCADE, default="")
    SHOES_ID = models.ForeignKey(SHOES_TABLE, on_delete=models.CASCADE,default="")
    COMMENT = models.CharField(max_length=300)

    def __str__(self):
        return self.COMMENT

class CONTACT_TABLE(models.Model):
    MESSAGE = models.CharField(max_length=300)
    FULL_NAME = models.CharField(max_length=300,default="")
    EMAIL_ID = models.EmailField()
    PHONE_NO = models.BigIntegerField()

    def __str__(self):
        return self.EMAIL_ID

class FEEDBACK(models.Model):
    L_ID = models.ForeignKey(LOGIN_TABLE, on_delete=models.CASCADE, default="")
    RATINGS = models.CharField(max_length=300)
    COMMENT = models.CharField(max_length=300, default="")

