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
    item = {'name':item.name,'kind':item.rank,'stat':json.loads(item.stats)}
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
    return JsonResponse(item,safe=False,json_dumps_params={'ensure_ascii': False})