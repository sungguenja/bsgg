from django.contrib import admin
from .models import Character, Ampli, Skill, Weapon, UsedWeapon, RealAmpli
# Register your models here.
admin.site.register(Character)
admin.site.register(Ampli)
admin.site.register(Skill)
admin.site.register(Weapon)
admin.site.register(UsedWeapon)
admin.site.register(RealAmpli)