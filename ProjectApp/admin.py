from django.contrib import admin
from .models import ServiceCategory, Service, Customer, ServiceSubCategory, ServicePricing, ServiceImage, Order


# Register your models here.

admin.site.register(ServiceCategory)
admin.site.register(Service)
admin.site.register(Customer)
admin.site.register(ServiceSubCategory)
admin.site.register(ServicePricing)
admin.site.register(ServiceImage)
admin.site.register(Order)
