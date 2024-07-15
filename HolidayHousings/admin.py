from django.contrib import admin
from HolidayHousings.models import HolidayHousing, Comment
from django.contrib import admin
#from .models import Product, CartItem
# Register your models here.
admin.site.register(HolidayHousing)
admin.site.register(Comment)
#admin.site.register(Product)
#admin.site.register(CartItem)
