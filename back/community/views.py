from django.shortcuts import render
from django.apps import apps
from django.core import serializers
from django.http import JsonResponse
from django.forms.models import model_to_dict
import json
from .models import *

# Create your views here.
def all_check(request,characweapon):
    data = []
    if characweapon==0:
        play_throughs = Playthrough.objects.all()
        play_throughs = serializers.serialize('json',play_throughs)
        play_throughs = json.loads(play_throughs)
        for article in play_throughs:
            data.append({'pk':article['pk'],'title':article['fields']['title']})
    else:
        characweapon_list = apps.get_model('characters','UsedWeapon').objects.filter(charac=characweapon)
        for characweapon in characweapon_list:
            play_throughs = Playthrough.objects.filter(characweapon=characweapon.id)
            play_throughs = serializers.serialize('json',play_throughs)
            play_throughs = json.loads(play_throughs)
            for article in play_throughs:
                data.append({'pk':article['pk'],'title':article['fields']['title']})
    return JsonResponse(data,safe=False,json_dumps_params={'ensure_ascii': False})

def gamedata(request,pk):
    characweapon = apps.get_model('characters','UsedWeapon').objects.get(pk=pk)
    item_list = apps.get_model('gamedata','Item').objects.all()

    weapon_kind_pk = characweapon.weapon_name.pk
    armor_kind_pk  = 22
    head_kind_pk   = 21
    arm_kind_pk    = 23
    leg_kind_pk    = 24
    acc_kind_pk    = 25
    weapon_list    = []
    armor_list     = []
    head_list      = []
    arm_list       = []
    leg_list       = []
    accessory_list = []

    life_tree_pk     = 343
    life_dust_pk     = 373
    eternal_ice_pk   = 490
    samadhi_fire_pk  = 491
    meteor_pk        = 210
    mithril_pk       = 347
    blood_pk         = 350
    moon_stone_pk    = 344
    force_core_pk    = 497
    life_tree_list   = []
    meteor_list      = []
    mithril_list     = []
    blood_list       = []
    moon_stone_list  = []
    force_core_list  = []

    for item in item_list:
        trigger = False
        item_kinds = item.kinds
        if item_kinds == weapon_kind_pk:
            trigger = True
            weapon_list.append({'pk':item.pk,'kinds':item_kinds,'rank':item.rank,'name':item.name,'stats':json.loads(item.stats)})
        elif item_kinds == armor_kind_pk:
            trigger = True
            armor_list.append({'pk':item.pk,'kinds':item_kinds,'rank':item.rank,'name':item.name,'stats':json.loads(item.stats)})
        elif item_kinds == head_kind_pk:
            trigger = True
            head_list.append({'pk':item.pk,'kinds':item_kinds,'rank':item.rank,'name':item.name,'stats':json.loads(item.stats)})
        elif item_kinds == arm_kind_pk:
            trigger = True
            arm_list.append({'pk':item.pk,'kinds':item_kinds,'rank':item.rank,'name':item.name,'stats':json.loads(item.stats)})
        elif item_kinds == leg_kind_pk:
            trigger = True
            leg_list.append({'pk':item.pk,'kinds':item_kinds,'rank':item.rank,'name':item.name,'stats':json.loads(item.stats)})
        elif item_kinds == acc_kind_pk:
            trigger = True
            accessory_list.append({'pk':item.pk,'kinds':item_kinds,'rank':item.rank,'name':item.name,'stats':json.loads(item.stats)})
        if trigger:
            item_left_pk  = item.material_left
            item_right_pk = item.material_right
            if item_left_pk == life_tree_pk or item_left_pk == life_dust_pk or item_left_pk == eternal_ice_pk or item_left_pk == samadhi_fire_pk or item_right_pk == life_tree_pk or item_right_pk  == life_dust_pk or item_right_pk == eternal_ice_pk or item_right_pk == samadhi_fire_pk:
                life_tree_list.append({'pk':item.pk,'kinds':item_kinds,'rank':item.rank,'name':item.name,'stats':json.loads(item.stats)})
            elif item_left_pk == meteor_pk or item_right_pk == meteor_pk:
                meteor_list.append({'pk':item.pk,'kinds':item_kinds,'rank':item.rank,'name':item.name,'stats':json.loads(item.stats)})
            elif item_left_pk == mithril_pk or item_right_pk == mithril_pk:
                mithril_list.append({'pk':item.pk,'kinds':item_kinds,'rank':item.rank,'name':item.name,'stats':json.loads(item.stats)})
            elif item_left_pk == blood_pk or item_right_pk == blood_pk:
                blood_list.append({'pk':item.pk,'kinds':item_kinds,'rank':item.rank,'name':item.name,'stats':json.loads(item.stats)})
            elif item_left_pk == moon_stone_pk or item_right_pk == moon_stone_pk:
                moon_stone_list.append({'pk':item.pk,'kinds':item_kinds,'rank':item.rank,'name':item.name,'stats':json.loads(item.stats)})
            elif item_left_pk == force_core_pk or item_right_pk == force_core_pk:
                force_core_list.append({'pk':item.pk,'kinds':item_kinds,'rank':item.rank,'name':item.name,'stats':json.loads(item.stats)})
    
    character = characweapon.charac

    skill_list = apps.get_model('characters','Skill').objects.filter(charac=character.pk)
    skill_list = my_serializer(skill_list)

    map_list = apps.get_model('gamedata','Area').objects.all()
    map_list = my_serializer(map_list)

    character = serializers.serialize('json',[character])
    character = json.loads(character)

    response = {
        'weapon_list'    : weapon_list,
        'armor_list'     : armor_list,
        'head_list'      : head_list,
        'arm_list'       : arm_list,
        'leg_list'       : leg_list,
        'accessory_list' : accessory_list,
        'life_tree_list' : life_tree_list,
        'meteor_list'    : meteor_list,
        'mithril_list'   : mithril_list,
        'blood_list'     : blood_list,
        'moon_stone_list': moon_stone_list,
        'force_core_list': force_core_list,
        'skill_list'     : skill_list,
        'map_list'       : map_list,
        'character'      : character
    }
    
    return JsonResponse(response,safe=False,json_dumps_params={'ensure_ascii': False})

def my_serializer(target):
    result = serializers.serialize('json',target)
    result = json.loads(result)
    return result