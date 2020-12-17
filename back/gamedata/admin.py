from django.contrib import admin
from .models import Area, Animal, Item, AreaItem, AreaAnimal, AnimalItem
# Register your models here.
admin.site.register(Area)
admin.site.register(Animal)
admin.site.register(Item)
admin.site.register(AreaItem)
admin.site.register(AreaAnimal)
admin.site.register(AnimalItem)