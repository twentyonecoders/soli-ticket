from django.contrib import admin
from .models import Organiser, UserAddress, Order, Customer

admin.site.register(Organiser)
admin.site.register(UserAddress)
admin.site.register(Order)
admin.site.register(Customer)
