from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render
from .models import *
import json

# Create your views here.
def all_chr(request):
    characters = Character.objects.all()
    characters = serializers.serialize('json',characters)
    characters = json.loads(characters)
    data = []
    for char in characters:
        data.append({'pk':char['pk'],'name':char['fields']['name']})
    return JsonResponse(data,safe=False,json_dumps_params={'ensure_ascii': False})

def detail(request,pk):
    choosed_character = Character.objects.get(pk=pk)
    choosed_character = serializers.serialize('json',[choosed_character])
    choosed_character = json.loads(choosed_character)
    skills = Skill.objects.filter(charac=pk)
    skills = serializers.serialize('json',skills)
    skills = json.loads(skills)
    weapons = UsedWeapon.objects.filter(charac=pk)
    weapons = serializers.serialize('json',weapons)
    weapons = json.loads(weapons)
    ampli_stats = Ampli.objects.filter(charac=pk)
    ampli_stats = serializers.serialize('json',ampli_stats)
    ampli_stats = json.loads(ampli_stats)
    using_weapon_name = []
    for i in weapons:
        skill = find_skill_detail(i['fields']['weapon_name'])
        using_weapon_name.append({'name':find_weapon_name(i['fields']['weapon_name']),'pk':i['fields']['weapon_name'],'skill':skill})
    return JsonResponse({'character':choosed_character,'skills':skills,'weapons':using_weapon_name,'ampli':ampli_stats},safe=False,json_dumps_params={'ensure_ascii':False})

def find_weapon_name(pk):
    weapon_name = Weapon.objects.get(pk=pk)
    return weapon_name.name

def find_skill_detail(pk):
    weapon_skill = Weapon.objects.get(pk=pk)
    return weapon_skill.skill_detail

def detail_weapon(request,pk):
    weapon_detail = Weapon.objects.get(pk=pk)
    weapon_detail = serializers.serialize('json',[weapon_detail])
    weapon_detail = json.loads(weapon_detail)
    return JsonResponse(weapon_detail,safe=False,json_dumps_params={'ensure_ascii':False})