from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render
from django.forms.models import model_to_dict
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
    item = Item.objects.get(name=item_name)
    item = {'name':item.name,'kind':item.rank,'stat':json.loads(item.stats),'pk':item.pk}
    return JsonResponse(item,safe=False,json_dumps_params={'ensure_ascii': False})

def search_category(request,category_type):
    total_item = Item.objects.filter(kinds=category_type)
    data = {'items':[]}
    for it in total_item:
        now = {}
        now['name'] = it.name
        now['kinds'] = it.kinds
        now['rank'] = it.rank
        now['pk'] = it.pk
        data['items'].append(now)
    return JsonResponse(data,safe=False,json_dumps_params={'ensure_ascii': False})

def item_detail(request,pk):
    item = Item.objects.get(pk=pk)
    item = model_to_dict(item)
    left_item_list = Item.objects.filter(material_left=pk)
    right_item_list = Item.objects.filter(material_right=pk)
    data = {'upper':[],'item':item}
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
    return JsonResponse(item,safe=False,json_dumps_params={'ensure_ascii': False})

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