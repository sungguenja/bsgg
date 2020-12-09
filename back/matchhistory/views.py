from django.http import JsonResponse
import requests, json
from bs4 import BeautifulSoup as bs
# Create your views here.
def searchhistory(request,user_name,season,team_mode):
    if request.method == 'GET':
        URL = 'http://matchhistory.playeternalreturn.com/'
        data = {'user_name':user_name,'season':season,'team_mode':team_mode}
        try:
            output = requests.post(URL+'statsKR_'+season,data=data).json()
            output = output['result']['output']
            soup_obj = bs(output,'html.parser')

            # 모스트 플레이
            most_played = soup_obj.find_all('div',{'class':'card'})
            most_played_character = []
            for i in range(len(most_played)):
                most_played_character.append({})
                most_played_character[i]['chr_name'] = most_played[i].find('h1').get_text()
                most_played_character[i]['chr_img'] = most_played[i].find('img')['src']
                most_played_character[i]['chr_cont'] = most_played[i].find('p',{'class':'title'}).get_text()
                top3_cnt = most_played[i].find('p',{'class':'subtitle'}).get_text()
                cnt = ''
                for j in range(-2,-len(top3_cnt),-1):
                    if top3_cnt[j] == ' ':
                        break
                    cnt = top3_cnt[j] + cnt
                most_played_character[i]['chr_top3'] = cnt

            # 총 통계
            avg_play = soup_obj.find_all('h4')
            win_cnt = avg_play[0].get_text()
            avg_win = avg_play[1].get_text()
            avg_kill = avg_play[2].get_text()

            # 캐릭터 별 통계
            avg_play = soup_obj.find('div',{'class':'grid'})
            charcater_statistics = []
            avg_play = avg_play.find_all('div')
            cnt = -1
            for i in range(len(avg_play)):
                if i&1:
                    now_text = avg_play[i].get_text()
                    now_text = list(now_text.split())
                    charcater_statistics[cnt]['chr_name'] = now_text[0][:-1]
                    charcater_statistics[cnt]['avg_win'] = now_text[1]
                    charcater_statistics[cnt]['max_kill'] = now_text[-1][:-1]
                else:
                    cnt += 1
                    charcater_statistics.append({})
                    charcater_statistics[cnt]['chr_img'] = avg_play[i].find('img')['src']

            # 최근 전적 20회
            avg_play = soup_obj.find_all('div',{'class':'gamecolumns container'})
            recent_match = []
            td_tag = soup_obj.find_all('td',{'class':'tdborder'})
            for i in range(len(avg_play)):
                recent_match.append({})
                recent_match[i]['date'] = avg_play[i].find('b').get_text()
                match_chr = avg_play[i].find('a')
                chr_name = ''
                go_name = False
                for j in range(len(match_chr['href'])):
                    if go_name:
                        chr_name += match_chr['href'][j]
                    else:
                        if match_chr['href'][j] == '=':
                            go_name = True
                recent_match[i]['chr_name'] = chr_name
                recent_match[i]['chr_img'] = match_chr.find('img')['src']
                recent_match[i]['level'] = td_tag[i*11+1].get_text()
                recent_match[i]['rank'] = td_tag[i*11+2].get_text()
                recent_match[i]['kill_cnt'] = td_tag[i*11+3].get_text()
                recent_match[i]['animal_cnt'] = td_tag[i*11+4].get_text()
                if td_tag[i*11+5].find('a') != None:
                    recent_match[i]['weapon'] = td_tag[i*11+5].find('a').get_text()
                    recent_match[i]['weapon_img'] = td_tag[i*11+5].find('img')['src']
                else:
                    recent_match[i]['weapon'] = None
                    recent_match[i]['weapon_img'] = None
                if td_tag[i*11+6].find('a') != None:
                    recent_match[i]['head'] = td_tag[i*11+6].find('a').get_text()
                    recent_match[i]['head_img'] = td_tag[i*11+6].find('img')['src']
                else:
                    recent_match[i]['head'] = None
                    recent_match[i]['head_img'] = None
                if td_tag[i*11+7].find('a') != None:
                    recent_match[i]['cloth'] = td_tag[i*11+7].find('a').get_text()
                    recent_match[i]['cloth_img'] = td_tag[i*11+7].find('img')['src']
                else:
                    recent_match[i]['cloth'] = None
                    recent_match[i]['cloth_img'] = None
                if td_tag[i*11+8].find('a') != None:
                    recent_match[i]['arm'] = td_tag[i*11+8].find('a').get_text()
                    recent_match[i]['arm_img'] = td_tag[i*11+8].find('img')['src']
                else:
                    recent_match[i]['arm'] = None
                    recent_match[i]['arm_img'] = None
                if td_tag[i*11+9].find('a') != None:
                    recent_match[i]['leg'] = td_tag[i*11+9].find('a').get_text()
                    recent_match[i]['leg_img'] = td_tag[i*11+9].find('img')['src']
                else:
                    recent_match[i]['leg'] = None
                    recent_match[i]['leg_img'] = None
                if td_tag[i*11+10].find('a') != None:
                    recent_match[i]['accessory'] = td_tag[i*11+10].find('a').get_text()
                    recent_match[i]['accessory_img'] = td_tag[i*11+10].find('img')['src']
                else:
                    recent_match[i]['accessory'] = None
                    recent_match[i]['accessory_img'] = None
            return JsonResponse({'success':1,'most_played':most_played_character,'character_statics':charcater_statistics,'total_statics':{'win_cnt':win_cnt,'avg_win':avg_win,'avg_kill':avg_kill},'recent_match':recent_match},safe=False,json_dumps_params={'ensure_ascii': False})
        except json.decoder.JSONDecodeError:
            return JsonResponse({'success':0})
    else:
        return JsonResponse({'굳이 이렇게 오시나요':request.method})