from bs4 import BeautifulSoup as bs
import requests, json
write_f = open('db_characters.txt','w',encoding='utf-8')
character_list = [0,'재키','아야','현우','매그너스','피오라','나딘','자히르','하트','아이솔','리 다이린','유키','혜진','쇼우','시셀라','키아라','아드리아나','쇼이치','실비아']
weapons = ['단검','양손검','도끼','쌍검','권총','돌격 소총','저격총','레이피어','창','망치','방망이','투척','암기','활','석궁','글러브','톤파','기타','쌍절곤','채찍']
for chr_id in range(1,len(character_list)):
    html_code = requests.get('https://eternalreturn-ko.gamepedia.com/{0}'.format(character_list[chr_id]))
    soup_obj = bs(html_code.text,'html.parser')
    table_objs = soup_obj.find_all('table')
    chr_text = "insert into characters_character ('name','attack','attack_growth','shield','shield_growth','health','health_growth',health_regen','health_regen_growth','stamina','stamina_growth','stamina_regen','stamina_regen_growth','attack_speed','attack_speed_growth','critical','critical_growth','moving_speed','moving_speed_growth','eyesight','eyesight_growth') values ("
    weapon_text = "insert into characters_usedweapon ('charac_id','weapon_name_id') values ("
    skill_text = "insert into characters_skill ('name','button','stats','detail','is_basic','charac_id') values ("
    ampli_duo = "insert into characters_ampli ('mode','damage_taken','damage_done','charac_id') values ('Duo',"
    ampli_trio = "insert into characters_ampli ('mode','damage_taken','damage_done','charac_id') values ('Trio',"
    for i in range(len(table_objs)):
        if i == 0:
            name = character_list[chr_id]
            chr_text += "'{0}',".format(name)
        elif i == 1:
            stats_tds = table_objs[i].find_all('td')
            attack = stats_tds[1].get_text().rstrip()
            attack_growth = stats_tds[3].get_text().rstrip()
            health = stats_tds[5].get_text().rstrip()
            health_growth = stats_tds[7].get_text().rstrip()
            health_regen = stats_tds[9].get_text().rstrip()
            health_regen_growth = stats_tds[11].get_text().rstrip()
            stamina = stats_tds[13].get_text().rstrip()
            stamina_growth = stats_tds[15].get_text().rstrip()
            stamina_regen = stats_tds[17].get_text().rstrip()
            stamina_regen_growth = stats_tds[19].get_text().rstrip()
            shield = stats_tds[21].get_text().rstrip()
            shield_growth = stats_tds[23].get_text().rstrip()
            attack_speed = stats_tds[25].get_text().rstrip()
            attack_speed_growth = 0
            critical = 0
            critical_growth = 0
            moving_speed = stats_tds[33].get_text().rstrip()
            moving_speed_growth = 0
            eyesight = 8
            eyesight_growth = 0
            chr_text += "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15},{16},{17},{18},{19});\n".format(attack,attack_growth,shield,shield_growth,health,health_growth,health_regen,health_regen_growth,stamina,stamina_growth,stamina_regen,stamina_regen_growth,attack_speed,attack_speed_growth,critical,critical_growth,moving_speed,moving_speed_growth,eyesight,eyesight_growth)
            write_f.write(chr_text)
        elif i==3:
            ampli_objs = table_objs[i].find_all('td')
            ampli_duo += ampli_objs[1].get_text()[:-1] + "," + ampli_objs[4].get_text()[:-1] + "," + str(chr_id) + ");\n"
            ampli_trio += ampli_objs[2].get_text()[:-1] + "," + ampli_objs[5].get_text()[:-1] + "," + str(chr_id) + ");\n" 
            write_f.write(ampli_duo)
            write_f.write(ampli_trio)
        elif i==len(table_objs)-1:
            weapon_list = table_objs[i].find_all('a',{'title':'무기'})
            for j in range(len(weapon_list)):
                weapon_text = "insert into characters_usedweapon ('charac_id','weapon_name_id') values ({0},{1});\n".format(chr_id,weapons.index(weapon_list[j].get_text()))
                write_f.write(weapon_text)
        else:
            if i%2 == 1:
                continue
            skill_name = table_objs[i].find('span',{"class":"mw-headline"})
            if skill_name == None:
                continue
            skill_name = skill_name.get_text()
            skill_stats = table_objs[i].find('table')
            skill_stats = skill_stats.find_all('td')
            skill_stats_text = "{"
            button = '패시브'
            if '-' in skill_name:
                button = skill_name[0]
                skill_name = skill_name[4:]
            elif '(' in skill_name:
                button = skill_name[skill_name.find('(')+1:-1]
                skill_name = skill_name[:skill_name.find('(')]
            for j in range(len(skill_stats)):
                if j%2==0:
                    skill_stats_text +=  '"' + skill_stats[j].get_text() + '"' + ':'
                else:
                    skill_stats_text += '"' + skill_stats[j].get_text() + '",'
            skill_stats_text = skill_stats_text[:-1] + "}"
            skill_detail = table_objs[i].find('div',{'style':'margin:1em'}).get_text()
            skill_text += "'{0}','{4}','{1}','{2}','basic',{3});\n".format(skill_name,skill_stats_text,skill_detail[1:],chr_id,button)
            write_f.write(skill_text)
            skill_text = "insert into characters_skill ('name','button','stats','detail','is_basic','charac_id') values ("