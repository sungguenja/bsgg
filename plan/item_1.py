# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
import requests, json
url = 'https://eternalreturn-ko.gamepedia.com/'
item = requests.get('http://127.0.0.1:8000/gamedata/')
item = item.json()
write_f = open('item_third.txt','w',encoding='utf-8')
kinds = [0,'단검','양손검','도끼','쌍검','권총','돌격소총','저격총','레이피어','창','망치','방망이','투척','암기','활','석궁','글러브','톤파','기타','쌍절곤','채찍','머리','옷','팔','다리','장식','음식','음료','설치','재료']
items = ['군용_나이프','샴쉬르','사슬_낫','전투_도끼','쌍칼','매그넘-파이선','베레타_M92F','STG-44','스프링필드','레이피어','죽창','워해머','장봉','수류탄','화염병','싸인볼','다트','빈티지_카드','표창','흑건','목궁','장궁','쇠뇌','크로스보우','글러브','아이언_너클','톤파','골든_브릿지','싱글_픽업','눈차크','오랏줄','철편','가면','머리테','베레모','사슬_코이프','안전모','가죽_갑옷','가죽_자켓','거북_도복','군복','덧댄_로브','드레스','비키니','잠수복','가죽_방패','분대장_완장','브레이서','무릎_보호대','체인_레깅스','하이힐','힐리스','덧댄_슬리퍼','군선','성자의_유산','운명의_꽃','유리_조각','인형','저격_스코프','진신사리','화살통','먼지털이개','꿀_바른_대구살','대구_간_통조림','마늘빵','버터','보약','붕어빵','성수','지혈제','초코파이','한방침','난초','탄두리','마늘_베이컨_말이','번','햄버거','감자빵','감자스프','달걀_생선_필레','시트러스_케이크','레몬_아이스크림','마늘_꿀절임','계란빵','이스터_에그','위스키_봉봉','초코_아이스크림','카레빵','뜨거운_물','레몬에이드','물병','백주','소주','아이스_커피','칵테일','커피_리큐르','콜라','카페라테','꿀탄_우유','하이볼','초코_우유','꿀물','얼음물','온더락','카우보이','가시_발판','개량형_쥐덫','다이너마이트','대나무_트랩','부비트랩','소란_발생기','망원_카메라','정글_기요틴','폭발_트랩','강철','기름먹인_천','뜨거운_오일','루비','방전_전지','백색_가루','달궈진_돌멩이','운석','재','전자_부품','정교한_도면','철판','황금']
for j in range(len(items)):
    item_html = requests.get(url+items[j])
    item_html = bs(item_html.text,'html.parser')
    tables = item_html.find_all('table')
    item_stat = tables[0].find_all('center')
    name = item_stat[0].get_text()
    try:
        kind = item_stat[1].find('a').get_text()
    except AttributeError:
        print(items[j])
        continue
    kind = kinds.index(kind)
    stats = tables[0].find_all('li')
    stat = {}
    for i in range(len(stats)):
        stats_text = stats[i].get_text()
        if '+' in stats_text:
            key,value = stats_text.split('+')
            key = key[:-1]
            key = '"{}"'.format(key)
            value = '+'+value
            value = '"{}"'.format(value)
            stat[key] = value
        elif '-' in stats_text:
            key,value = stats_text.split('-')
            key = key[:-1]
            value = '-'+value
            key = '"{}"'.format(key)
            value = '"{}"'.format(value)
            stat[key] = value
    table_1 = tables[1].find_all('a')
    try:
        left = table_1[1]['title']
        right = table_1[3]['title']
    except KeyError:
        print(items[j])
        continue
    for i in range(len(item)):
        if item[i]['fields']['name'] == left:
            left = item[i]['pk']
        if item[i]['fields']['name'] == right:
            right = item[i]['pk']
        if type(left) == int and type(right) == int:
            break
    write_f.write("insert into gamedata_item ('name','kinds','rank','max_quantity','stats','material_left','material_right') values ('{0}',{1},1,1,'{2}',{3},{4});\n".format(name,kind,stat,left,right))