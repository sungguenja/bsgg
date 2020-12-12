from bs4 import BeautifulSoup as bs
import requests, json
write_f = open('item_second.txt','w',encoding='utf-8')
area = [0,'골목길','절','번화가','연못','병원','양궁장','학교','묘지','공장','호텔','숲','성당','모래사장','고급 주택가','항구','연구소']
item = requests.get('http://127.0.0.1:8000/gamedata/')
item = item.json()
animal = {'닭':1,'박쥐':2,'멧돼지':3,'들개':4,'늑대':5,'곰':6,'위클라인':7}
for j in range(1,len(area)):
    area_html = requests.get('https://eternalreturn-ko.gamepedia.com/{}'.format(area[j]))
    area_html = bs(area_html.text,'html.parser')
    area_html = area_html.find_all('table')
    item_cnt = area_html[1].find_all('td')
    for i in range(0,len(item_cnt),2):
        item_name = item_cnt[i].get_text()
        item_name = list(item_name.split('\n'))[0]
        icnt = list(item_cnt[i+1].get_text().split('\n'))[0]
        for i_pk in range(len(item)):
            if item[i_pk]['fields']['name'] == item_name:
                write_f.write("insert into gamedata_areaitem ('quantity','area_id_id','item_id_id') values ({0},{1},{2});\n".format(icnt,j,item[i_pk]['pk']))
                break
    animal_cnt = area_html[2].find_all('td')
    for i in range(0,len(animal_cnt),2):
        animal_name = animal_cnt[i].get_text()
        animal_name = list(animal_name.split('\n'))[0]
        acnt = list(animal_cnt[i+1].get_text().split('\n'))[0]
        write_f.write("insert into gamedata_areaanimal ('respon_amount','animal_id_id','area_id_id') values ({0},{1},{2});\n".format(acnt,animal.get(animal_name),j))