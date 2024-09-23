from django.contrib import admin

# Register your models here.

from userbookapp.models import Cart,CartItem

admin.site.register(Cart)
admin.site.register(CartItem)