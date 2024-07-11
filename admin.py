from django.contrib import admin
from .models import TodoItem
from .models import Broker
from .models import Seller

# Register your models here.
admin.site.register(TodoItem)
admin.site.register(Broker)
admin.site.register(Seller)
