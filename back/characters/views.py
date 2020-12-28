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
    cate = [0,'단검','양손검','도끼','쌍검','권총','돌격 소총','저격총','레이피어','창','망치','방망이','투척','암기','활','석궁','글러브','톤파','기타','쌍절곤','채찍','머리','옷','팔','다리','장식','음식','음료','설치','재료']
    choosed_character = Character.objects.get(pk=pk)
    choosed_character = serializers.serialize('json',[choosed_character])
    choosed_character = json.loads(choosed_character)
    skills = Skill.objects.filter(charac=pk)
    skills = serializers.serialize('json',skills)
    skills = json.loads(skills)
    weapons = UsedWeapon.objects.filter(charac=pk)
    weapons = serializers.serialize('json',weapons)
    weapons = json.loads(weapons)
    ampli_stats = []
    for k in weapons:
        data = {}
        now_ampli = ModeWeaponCharacterAmpli.objects.get(charac_weapon=k['pk'])
        now_ampli = serializers.serialize('json',[now_ampli])
        now_ampli = json.loads(now_ampli)
        now_ampli = now_ampli[0]
        data['weapon_type'] = cate[k['fields']['weapon_name']]
        data['SoloDamageTaken'] = now_ampli['fields']['SoloDamageTaken']
        data['SoloDamageGive'] = now_ampli['fields']['SoloDamageGive']
        data['DuoDamageTaken'] = now_ampli['fields']['DuoDamageTaken']
        data['DuoDamageGive'] = now_ampli['fields']['DuoDamageGive']
        data['SquadDamageTaken'] = now_ampli['fields']['SquadDamageTaken']
        data['SquadDamageGive'] = now_ampli['fields']['SquadDamageGive']
        ampli_stats.append(data)
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