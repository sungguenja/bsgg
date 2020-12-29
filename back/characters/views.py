from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render
from django.db.models import Avg
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
    state_object = WeaponCharacterStat.objects.all()
    solo_state_all_avg_win = state_object.filter(is_ranker=0,mode='Solo').aggregate(Avg('win_rate'))
    solo_state_all_avg_pick = state_object.filter(is_ranker=0,mode='Solo').aggregate(Avg('pick_rate'))
    solo_state_all_avg_kill = state_object.filter(is_ranker=0,mode='Solo').aggregate(Avg('avg_kill'))
    solo_state_all_avg_rank = state_object.filter(is_ranker=0,mode='Solo').aggregate(Avg('avg_rank'))
    solo_state_ranker_avg_win = state_object.filter(is_ranker=1,mode='Solo').aggregate(Avg('win_rate'))
    solo_state_ranker_avg_pick = state_object.filter(is_ranker=1,mode='Solo').aggregate(Avg('pick_rate'))
    solo_state_ranker_avg_kill = state_object.filter(is_ranker=1,mode='Solo').aggregate(Avg('avg_kill'))
    solo_state_ranker_avg_rank = state_object.filter(is_ranker=1,mode='Solo').aggregate(Avg('avg_rank'))

    duo_state_all_avg_win = state_object.filter(is_ranker=0,mode='Duo').aggregate(Avg('win_rate'))
    duo_state_all_avg_pick = state_object.filter(is_ranker=0,mode='Duo').aggregate(Avg('pick_rate'))
    duo_state_all_avg_kill = state_object.filter(is_ranker=0,mode='Duo').aggregate(Avg('avg_kill'))
    duo_state_all_avg_rank = state_object.filter(is_ranker=0,mode='Duo').aggregate(Avg('avg_rank'))
    duo_state_ranker_avg_win = state_object.filter(is_ranker=1,mode='Duo').aggregate(Avg('win_rate'))
    duo_state_ranker_avg_pick = state_object.filter(is_ranker=1,mode='Duo').aggregate(Avg('pick_rate'))
    duo_state_ranker_avg_kill = state_object.filter(is_ranker=1,mode='Duo').aggregate(Avg('avg_kill'))
    duo_state_ranker_avg_rank = state_object.filter(is_ranker=1,mode='Duo').aggregate(Avg('avg_rank'))

    squad_state_all_avg_win = state_object.filter(is_ranker=0,mode='Squad').aggregate(Avg('win_rate'))
    squad_state_all_avg_pick = state_object.filter(is_ranker=0,mode='Squad').aggregate(Avg('pick_rate'))
    squad_state_all_avg_kill = state_object.filter(is_ranker=0,mode='Squad').aggregate(Avg('avg_kill'))
    squad_state_all_avg_rank = state_object.filter(is_ranker=0,mode='Squad').aggregate(Avg('avg_rank'))
    squad_state_ranker_avg_win = state_object.filter(is_ranker=1,mode='Squad').aggregate(Avg('win_rate'))
    squad_state_ranker_avg_pick = state_object.filter(is_ranker=1,mode='Squad').aggregate(Avg('pick_rate'))
    squad_state_ranker_avg_kill = state_object.filter(is_ranker=1,mode='Squad').aggregate(Avg('avg_kill'))
    squad_state_ranker_avg_rank = state_object.filter(is_ranker=1,mode='Squad').aggregate(Avg('avg_rank'))

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
    state_all = {
      'solo_avg_win':solo_state_all_avg_win['win_rate__avg'],
      'solo_avg_pick':solo_state_all_avg_pick['pick_rate__avg'],
      'solo_avg_kill':solo_state_all_avg_kill['avg_kill__avg'],
      'solo_avg_rank':solo_state_all_avg_rank['avg_rank__avg'],
      'duo_avg_win':duo_state_all_avg_win['win_rate__avg'],
      'duo_avg_pick':duo_state_all_avg_pick['pick_rate__avg'],
      'duo_avg_kill':duo_state_all_avg_kill['avg_kill__avg'],
      'duo_avg_rank':duo_state_all_avg_rank['avg_rank__avg'],
      'squad_avg_win':squad_state_all_avg_win['win_rate__avg'],
      'squad_avg_pick':squad_state_all_avg_pick['pick_rate__avg'],
      'squad_avg_kill':squad_state_all_avg_kill['avg_kill__avg'],
      'squad_avg_rank':squad_state_all_avg_rank['avg_rank__avg']
    }
    state_ranker = {
      'solo_avg_win':solo_state_ranker_avg_win['win_rate__avg'],
      'solo_avg_pick':solo_state_ranker_avg_pick['pick_rate__avg'],
      'solo_avg_kill':solo_state_ranker_avg_kill['avg_kill__avg'],
      'solo_avg_rank':solo_state_ranker_avg_rank['avg_rank__avg'],
      'duo_avg_win':duo_state_ranker_avg_win['win_rate__avg'],
      'duo_avg_pick':duo_state_ranker_avg_pick['pick_rate__avg'],
      'duo_avg_kill':duo_state_ranker_avg_kill['avg_kill__avg'],
      'duo_avg_rank':duo_state_ranker_avg_rank['avg_rank__avg'],
      'squad_avg_win':squad_state_ranker_avg_win['win_rate__avg'],
      'squad_avg_pick':squad_state_ranker_avg_pick['pick_rate__avg'],
      'squad_avg_kill':squad_state_ranker_avg_kill['avg_kill__avg'],
      'squad_avg_rank':squad_state_ranker_avg_rank['avg_rank__avg']
    }
    weapon_stat = []
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
        now_stat = WeaponCharacterStat.objects.filter(charac_weapon=k['pk'])
        now_stat = serializers.serialize('json',now_stat)
        now_stat = json.loads(now_stat)
        for l in now_stat:
            stat_data = {}
            stat_data['mode'] = l['fields']['mode']
            stat_data['is_ranker'] = l['fields']['is_ranker']
            stat_data['win_rate'] = l['fields']['win_rate']
            stat_data['win_rate_rank'] = list(state_object.filter(is_ranker=stat_data['is_ranker'],mode=stat_data['mode']).order_by('-win_rate').values_list('win_rate',flat=True)).index(stat_data['win_rate'])+1
            stat_data['pick_rate'] = l['fields']['pick_rate']
            stat_data['pick_rate_rank'] = list(state_object.filter(is_ranker=stat_data['is_ranker'],mode=stat_data['mode']).order_by('-pick_rate').values_list('pick_rate',flat=True)).index(stat_data['pick_rate'])+1
            stat_data['avg_kill'] = l['fields']['avg_kill']
            stat_data['avg_kill_rank'] = list(state_object.filter(is_ranker=stat_data['is_ranker'],mode=stat_data['mode']).order_by('-avg_kill').values_list('avg_kill',flat=True)).index(stat_data['avg_kill'])+1
            stat_data['avg_rank'] = l['fields']['avg_rank']
            stat_data['avg_rank_rank'] = list(state_object.filter(is_ranker=stat_data['is_ranker'],mode=stat_data['mode']).order_by('-avg_rank').values_list('avg_rank',flat=True)).index(stat_data['avg_rank'])+1
            stat_data['cate'] = cate[k['fields']['weapon_name']]
            weapon_stat.append(stat_data)
    using_weapon_name = []
    for i in weapons:
        skill = find_skill_detail(i['fields']['weapon_name'])
        using_weapon_name.append({'name':find_weapon_name(i['fields']['weapon_name']),'pk':i['fields']['weapon_name'],'skill':skill})
    return JsonResponse({'character':choosed_character,'skills':skills,'weapons':using_weapon_name,'ampli':ampli_stats,'stat':weapon_stat,'all_state':state_all,'ranker_state':state_ranker},safe=False,json_dumps_params={'ensure_ascii':False})

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