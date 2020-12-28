from django.contrib import admin
from .models import Character, Skill, Weapon, UsedWeapon, ModeWeaponCharacterAmpli, WeaponCharacterStat, WeaponStat, ArmorStat
# Register your models here.
admin.site.register(Character)
admin.site.register(Skill)
admin.site.register(Weapon)
admin.site.register(UsedWeapon)
admin.site.register(ModeWeaponCharacterAmpli)
admin.site.register(WeaponCharacterStat)
admin.site.register(WeaponStat)
admin.site.register(ArmorStat)