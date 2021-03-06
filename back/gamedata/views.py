from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render
from django.forms.models import model_to_dict
from django.apps import apps
from .models import *
import json

# Create your views here.
def all_item(request):
    all_item = Item.objects.all()
    characters = serializers.serialize('json',all_item)
    characters = json.loads(characters)
    return JsonResponse(characters,safe=False,json_dumps_params={'ensure_ascii': False})

def search_item(request,item_name):
    if item_name == '광학미채 수트':
        item_name = '광학미채 슈트'
    elif item_name == '유리조각':
        item_name = '유리 조각'
    elif item_name == '상자':
        item_name = '상자(장식)'
    elif item_name == '매버릭러너':
        item_name = '매버릭 러너'
    elif item_name == '배틀 수트':
        item_name = '배틀 슈트'
    elif item_name == '운명의꽃':
        item_name = '운명의 꽃'
    elif item_name == '플레솃':
        item_name = '플레셋'
    elif item_name == '녹슨검':
        item_name = '녹슨 검'
    item = Item.objects.get(name=item_name)
    item = {'name':item.name,'kind':item.rank,'stat':json.loads(item.stats),'pk':item.pk}
    return JsonResponse(item,safe=False,json_dumps_params={'ensure_ascii': False})

def search_category(request,category_type):
    total_item = Item.objects.filter(kinds=category_type).order_by("rank")
    data = {'items':[],'stats':[]}
    for it in total_item:
        now = {}
        now['name'] = it.name
        now['kinds'] = it.kinds
        now['rank'] = it.rank
        now['pk'] = it.pk
        data['items'].append(now)
        stats = apps.get_model('characters','ArmorStat').objects.filter(item=it.pk)
        for stat in stats:
            data['stats'].append({'name':it.name,'solo':stat.solo_win,'duo':stat.duo_win,'squad':stat.squad_win})
    return JsonResponse(data,safe=False,json_dumps_params={'ensure_ascii': False})

def item_detail(request,pk):
    item = Item.objects.get(pk=pk)
    item = model_to_dict(item)
    left_item_list = Item.objects.filter(material_left=pk)
    right_item_list = Item.objects.filter(material_right=pk)
    area_list = AreaItem.objects.filter(item_id=pk)
    animal_list = AnimalItem.objects.filter(item_id=pk)
    weapon_stat = apps.get_model('characters','WeaponStat').objects.filter(item=pk)
    statistcs = []
    for i in weapon_stat:
        for j in statistcs:
            if j['character'] == i.charac_weapon.charac.name:
                j[i.mode] = {'win_rate':i.win_rate,'pick_rate':i.pick_rate}
                break
        else:
            statistcs.append({})
            statistcs[-1]['character'] = i.charac_weapon.charac.name
            statistcs[-1][i.mode] = {'win_rate':i.win_rate,'pick_rate':i.pick_rate}
    armor_stats = []
    arm_st = apps.get_model('characters','ArmorStat').objects.filter(item=pk)
    for i in arm_st:
        armor_stats.append({'solo':i.solo_win,'duo':i.duo_win,'squad':i.squad_win})
    data = {'upper':[],'item':item,'animal':[],'area':[],'statistics':statistcs,'armor_stats':armor_stats}
    for it in left_item_list:
        now = {}
        now['name'] = it.name
        now['kinds'] = it.kinds
        now['rank'] = it.rank
        now['pk'] = it.pk
        data['upper'].append(now)
    for it in right_item_list:
        now = {}
        now['name'] = it.name
        now['kinds'] = it.kinds
        now['rank'] = it.rank
        now['pk'] = it.pk
        data['upper'].append(now)
    for it in area_list:
        now = {}
        now['name'] = it.area_id.name
        now['quantity'] = it.quantity
        now['pk'] = it.area_id.pk
        data['area'].append(now)
    for it in animal_list:
        now = {}
        now['name'] = it.animal_id.name
        now['pk'] = it.animal_id.pk
        data['animal'].append(now)
    return JsonResponse(data,safe=False,json_dumps_params={'ensure_ascii': False})

def only_that(request,pk):
    item = Item.objects.get(pk=pk)
    item = serializers.serialize('json',[item])
    item = json.loads(item)
    get_area = AreaItem.objects.filter(item_id=pk)
    get_area = serializers.serialize('json',get_area)
    get_area = json.loads(get_area)
    item[0]['area'] = []
    for i in get_area:
        area = Area.objects.get(pk=i['fields']['area_id'])
        item[0]['area'].append({'name':area.name,'quantity':i['fields']['quantity']})
    return JsonResponse(item[0],safe=False,json_dumps_params={'ensure_ascii': False})

def all_area(request,pk):
    data = []
    if pk == 0:
        area_data = Area.objects.all()
        for i in range(len(area_data)):
            now = {}
            now['pk'] = area_data[i].pk
            now['name'] = area_data[i].name
            data.append(now)
    else:
        data = {}
        area_data = Area.objects.get(pk=pk)
        item_data = AreaItem.objects.filter(area_id=pk)
        animal_data = AreaAnimal.objects.filter(area_id=pk)
        data['pk'] = area_data.pk
        data['name'] = area_data.name
        data['items'] = []
        for i in item_data:
            now = {}
            now['name'] = i.item_id.name
            now['pk'] = i.item_id.pk
            now['quantity'] = i.quantity
            now['kinds'] = i.item_id.kinds
            data['items'].append(now)
        data['animal'] = []
        for j in animal_data:
            now = {}
            now['name'] = j.animal_id.name
            now['pk'] = j.animal_id.pk
            now['respon'] = j.respon_amount
            data['animal'].append(now)
    return JsonResponse(data,safe=False,json_dumps_params={'ensure_ascii': False})

def animal_detail(request,pk):
    data = {'animal':None,'items':[],'areas':[]}
    animal = Animal.objects.get(pk=pk)
    animal = model_to_dict(animal)
    data['animal'] = animal
    items = AnimalItem.objects.filter(animal_id=pk)
    for it in items:
        now = {}
        now['name'] = it.item_id.name
        now['kinds'] = it.item_id.kinds
        now['rank'] = it.item_id.rank
        now['percentage'] = it.get_percent
        now['socket'] = it.pocket_number
        now['pk'] = it.item_id.pk
        data['items'].append(now)
    areas = AreaAnimal.objects.filter(animal_id=pk)
    for it in areas:
        now = {}
        now['name'] = it.area_id.name
        now['respon'] = it.respon_amount
        now['pk'] = it.area_id.pk
        data['areas'].append(now)
    return JsonResponse(data,safe=False,json_dumps_params={'ensure_ascii': False})