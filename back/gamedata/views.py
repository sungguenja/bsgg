from django.http import JsonResponse,Http404
from django.core import serializers
from django.shortcuts import render
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
    item = Item.objects.get(name=item_name)
    item = {'name':item.name,'kind':item.rank,'stat':json.loads(item.stats)}
    return JsonResponse(item,safe=False,json_dumps_params={'ensure_ascii': False})