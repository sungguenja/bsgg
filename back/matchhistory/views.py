from django.http import JsonResponse
from django.conf import settings
import requests, json
from bs4 import BeautifulSoup as bs
# Create your views here.
def searchhistory(request,user_name,season,team_mode):
    if request.method == 'GET':
        URL = 'https://open-api.bser.io/v1/user/'
        data = {'user_name':user_name,'season':season,'team_mode':team_mode}
        header = {"accept":"application/json","x-api-key":settings.BSER_KEY}
        cha_code = [0,'재키','아야','피오라','매그너스','자히르','나딘','현우','하트','아이솔','리 다이린','유키','혜진','쇼우','키아라','시셀라','실비아','아드리아나','쇼이치','엠마','레녹스','로지','루크','캐시']
        item_code = {201101: '머리띠', 201102: '모자', 201104: '자전거 헬멧', 201201: '가면', 201202: '머리테', 201203: '베레모', 201204: '사슬 코이프', 201205: '안전모', 201301: '방탄모', 201302: '소방 헬멧', 201303: '티아라', 201401: '왕관', 201402: '투구', 201403: '미스릴 투구', 201404: '수정 티아라', 201405: '오토바이 헬멧', 201406: '전술-OPS 헬멧', 201407: '기사단장의 투구', 201408: '월계관', 201409: '제국 왕관', 201410: '황실 부르고넷', 201411: '변검', 202101: '바람막이', 202103: '승복', 202105: '전신 수영복', 202106: '천 갑옷', 202201: '가죽 갑옷', 202202: '가죽 자켓', 202203: '거북 도복', 202205: '군복', 202206: '덧댄 로브', 202207: '드레스', 202209: '비키니', 202210: '잠수복', 202301: '라이더 자켓', 202302: '사슬 갑옷', 202303: '정장', 202304: '치파오', 202305: '판금 갑옷', 202306: '한복', 202401: '방탄조끼', 202402: '석양의 갑옷', 202404: '어사의', 202405: '광학미채 슈트', 202406: '락커의 자켓', 202407: '미스릴 갑옷', 202408: '성기사의 갑옷', 202410: '아마조네스 아머', 202411: '용의 도복', 202412: '지휘관의 갑옷', 202413: '집사복', 202415: '배틀 슈트', 202416: '불꽃 드레스', 202417: 'EOD 슈트', 202501: '카바나', 202502: '퀸 오브 하트', 203101: '손목시계', 203102: '붕대', 203104: '팔찌', 203201: '가죽 방패', 203202: '분대장 완장', 203203: '브레이서', 203301: '검집', 203302: '금팔찌', 203303: '바주반드', 203304: '진홍 팔찌', 203401: '강철 방패', 203402: '소드 스토퍼', 203403: '드라우프니르', 203404: '미스릴 방패', 203405: '바이탈 센서', 203406: '기사의 신조', 203407: '샤자한의 검집', 203408: '큐브 워치', 203501: '스카디의 팔찌', 203502: '레이더', 203503: '오토-암즈', 204101: '슬리퍼', 204102: '운동화', 204103: '타이즈', 204201: '무릎 보호대', 204202: '체인 레깅스', 204203: '하이힐', 204204: '힐리스', 204301: '덧댄 슬리퍼', 204302: '부츠', 204401: '강철 무릎 보호대', 204402: '경량화 부츠', 204403: '매버릭 러너', 204404: '전투화', 204405: '킬힐', 204406: '풍화륜', 204407: '미스릴 부츠', 204408: '부케팔로스', 204409: 'EOD 부츠', 204411: '클링온 부츠', 204410: '글레이셜 슈즈', 204501: '헤르메스의 부츠', 204502: '분홍신', 205101: '깃털', 205102: '꽃', 205103: '리본', 205105: '부채', 205106: '불경', 205107: '상자(장식)', 205108: '성배', 205109: '십자가', 205110: '쌍안경', 205202: '성자의 유산', 205203: '운명의 꽃', 205204: '유리 조각', 205205: '인형', 205206: '저격 스코프', 205207: '진신사리', 205208: '화살통', 205209: '먼지털이개', 205210: '군선', 205211: '비파단도', 205301: '생명의 가루', 205302: '우치와', 205303: '탄창', 205201: '백우선', 205401: '달빛 펜던트', 205304: '궁기병의 화살통', 205305: '월왕구천', 205404: '슈뢰딩거의 상자', 205405: '진리는 나의 빛', 205402: '만년빙', 205403: '삼매진화', 205501: '에메랄드 타블렛',101101: '가위', 101102: '만년필', 101104: '식칼', 101201: '군용 나이프', 101301: '장미칼', 101401: '카른웬난', 101402: '파산검', 101404: '초진동나이프', 101405: '프라가라흐', 102101: '녹슨 검', 102201: '샴쉬르', 102301: '일본도', 102401: '마사무네', 102402: '무라마사', 102403: '바스타드 소드', 102404: '보검', 102405: '뚜언 띠엔', 102406: '아론다이트', 102407: '엑스칼리버', 102408: '플라즈마 소드', 102409: '레바테인', 102410: '모노호시자오', 102411: '호푸어드', 102501: '다인슬라이프', 103201: '쌍칼', 103301: '피렌체식 쌍검', 103401: '이천일류', 103402: '자웅일대검', 103501: '디오스쿠로이', 103502: '로이거 차르', 104101: '망치', 104201: '워해머', 104301: '모닝 스타', 104302: '사슴 망치', 104401: '낭아봉', 104402: '다그다의 망치', 104403: '토르의 망치', 104404: '개밥바라기', 104405: '마법봉', 105102: '곡괭이', 105103: '손도끼', 105201: '사슬 낫', 105202: '전투 도끼', 105301: '경량화 도끼', 105302: '사신의 낫', 105401: '대부', 105402: '빔 엑스', 105403: '산타 무에르떼', 105404: '스퀴테', 105405: '파라슈', 105406: '하르페', 107101: '단창', 107201: '죽창', 107301: '바이던트', 107302: '파이크', 107303: '도끼창', 107401: '강창', 107402: '애각창', 107403: '장팔사모', 107404: '코스믹 바이던트', 107405: '트리아이나', 107406: '화첨창', 107407: '방천화극', 107408: '청룡언월도', 107501: '롱기누스의 창', 108101: '나뭇가지', 108102: '단봉', 108202: '장봉', 108301: '도깨비_방망이', 108401: '우산', 108402: '횃불', 108403: '구원의 여신상', 108404: '타구봉', 108501: '스파이의 우산', 108502: '여의봉', 109101: '채찍', 109201: '오랏줄', 109202: '철편', 109301: '바람채찍', 109401: '뇌룡편', 109402: '벽력편', 109403: '글레이프니르', 109404: '플라즈마윕', 109501: '혈화구절편', 110101: '너클', 110102: '목장갑', 110201: '글러브', 110202: '아이언 너클', 110301: '건틀릿', 110302: '윙 너클', 110401: '귀골 장갑', 110402: '벽력귀투', 110403: '유리 너클', 110404: '회단 장갑', 110405: '단영촌천투', 110406: '디바인 피스트', 110407: '블러드윙 너클', 110408: '빙화현옥수', 110409: '여래수투', 110410: '브레이질 건틀릿', 110411: '소수', 110412: '천잠장갑', 108103: '대나무', 111201: '톤파', 111301: '경찰봉', 111401: '류큐톤파', 111402: '택티컬 톤파', 111403: '마이쏙', 111404: '플라즈마 톤파', 112103: '쇠구슬', 112105: '야구공', 112202: '수류탄', 112203: '화염병', 112204: '슬링', 112205: '싸인볼', 112301: '밀가루 폭탄', 112302: '소이탄', 112303: '볼 라이트닝', 112304: '플러버', 112305: '안티오크의 수류탄', 112401: '다비드슬링', 112402: '연막탄', 112403: '가시 탱탱볼', 112404: '고폭 수류탄', 112501: '루테늄 구슬', 113101: '면도칼', 113102: '트럼프 카드', 113104: '분필', 113201: '다트', 113202: '부적', 113203: '빈티지 카드', 113205: '표창', 113206: '흑건', 113207: '유엽비도', 113301: '챠크람', 113302: '매화비표', 113401: '미치광이왕의 카드', 113402: '독침', 113403: '법륜', 113404: '플럼바타', 113405: '옥전결', 113406: '풍마 수리검', 113408: '빙백은침', 113409: '푸른색 단도', 113410: '플레솃', 113411: '건곤권', 113412: '생사부', 113501: '수다르사나', 113502: '만천화우', 114101: '양궁', 114201: '목궁', 114202: '장궁', 114203: '컴포지트 보우', 114301: '강궁', 114302: '국궁', 114303: '벽력궁', 114304: '탄궁', 114401: '편전', 114402: '화전', 114403: '골든래쇼 보우', 114405: '트윈보우', 114501: '엘리멘탈 보우', 114502: '페일노트', 115101: '석궁', 115201: '쇠뇌', 115202: '크로스보우', 115301: '노', 115302: '저격궁', 115303: '헤비 크로스보우', 115401: '철궁', 115402: '대황', 115403: '발리스타', 115404: '저격 크로스보우', 115405: '영광금귀신기노', 115501: '샤릉가', 116101: '발터 PPK', 116201: '매그넘-파이선', 116202: '베레타 M92F', 116301: 'FN57', 116401: '더블 리볼버 SP', 116402: '매그넘-아나콘다', 116403: '마탄의 사수', 116404: '엘레강스', 116405: '일렉트론 블라스터', 116406: '매그넘-보아', 116501: '악켈테', 117101: '페도로프 자동소총', 117201: 'STG-44', 117301: 'AK-47', 117401: 'M16A1', 117402: '기관총', 117403: '개틀링건', 117404: 'AK-12', 117405: 'XCR', 118101: '화승총', 118201: '스프링필드', 118301: '하푼건', 118401: '금교전', 118402: '레일건', 118403: 'Tac-50', 118404: '인터벤션', 118405: 'NTW-20', 118406: '폴라리스', 118501: '사사성광', 119101: '쇠사슬', 119201: '눈차크', 119301: '샤퍼', 119302: '블리더', 119401: '대소반룡곤', 119402: '초진동눈차크', 120101: '바늘', 120201: '레이피어', 120301: '매화검', 120302: '활빈검', 120401: '듀랜달 Mk2', 120402: '미스틸테인', 120403: '볼틱레토', 120404: '유성검', 120405: '주와이외즈', 121101: '보급형 기타', 121201: '골든 브릿지', 121202: '싱글 픽업', 121301: '루비 스페셜', 121302: '험버커 픽업', 121303: 'King-V', 121304: '노캐스터', 121305: '슈퍼스트랫', 121306: '야생마', 121401: '보헤미안', 121402: '천국의 계단', 121403: '퍼플 헤이즈', 121404: '새티스팩션', 121405: '원더풀 투나잇', 121406: '더 월', 121407: '틴 스피릿',205211:'비파단도',205305:'월왕구천',203409:'아이기스의 방패',203204:'고장난 시계',203410:'틴달로스의 팔찌',205212:'캐리비안 장식총',205306:'해적의 증표'}
        mastery_code = {1:'글러브',2:'톤파',3:'방망이',4:'채찍',5:'투척',6:'암기',7:'활',8:'석궁',9:'권총',10:'돌격 소총',11:'저격총',12:'캐논',13:'망치',14:'도끼',15:'단검',16:'양손검',17:'도끼',18:'쌍검',19:'창',20:'쌍절곤',21:'레이피어',22:'기타',101:'함정',102:'제작',103:'탐색',104:'이동',201:'체력',202:'방어',203:'명상',204:'함정'}
        # 스킬 1003500 이렇게 했을때 1003캐릭터(1000+캐릭터코드)500스킬(패시브qwer순으로100,200,300,400,500, 1,10의자리는 설명인듯)
        try:
            output = requests.get(URL+'nickname?query='+user_name,headers=header).json()
            if output['code'] != 200:
                return JsonResponse({'success':0})
            userNum = str(output['user']['userNum'])
            output = requests.get(URL+'games/'+userNum,headers=header).json()
            output = output['userGames']
            
            # 모스트 플레이
            most_played_rank = requests.get(URL+'stats/'+userNum+'/1',headers=header).json()
            most_played_normal = requests.get(URL+'stats/'+userNum+'/0',headers=header).json()
            most_played = {'rank':{},'normal':{}}
            # 총 통계
            if most_played_rank['code'] == 200:
                for i in most_played_rank['userStats']:
                    if i['matchingTeamMode'] == int(team_mode):
                        most_played['rank']['total_play'] = i['totalGames']
                        most_played['rank']['total_win'] = i['totalWins']
                        most_played['rank']['avg_rank'] = i['averageRank']
                        most_played['rank']['avg_kill'] = i['averageKills']
                        most_played['rank']['avg_assi'] = i['averageAssistants']
                        most_played['rank']['avg_hunt'] = i['averageHunts']
                        most_played['rank']['top3'] = i['top3']
                        most_played['rank']['top5'] = i['top5']
                        most_played['rank']['top7'] = i['top7']
                        most_played['rank']['character_statistics'] = []
                        for j in range(len(i['characterStats'])):
                            most_played['rank']['character_statistics'].append(i['characterStats'][j])
                            most_played['rank']['character_statistics'][j]['characterCode'] = cha_code[most_played['rank']['character_statistics'][j]['characterCode']]
            
            if most_played_normal['code'] == 200:
                for i in most_played_normal['userStats']:
                    if i['matchingTeamMode'] == int(team_mode):
                        most_played['normal']['total_play'] = i['totalGames']
                        most_played['normal']['total_win'] = i['totalWins']
                        most_played['normal']['avg_rank'] = i['averageRank']
                        most_played['normal']['avg_kill'] = i['averageKills']
                        most_played['normal']['avg_assi'] = i['averageAssistants']
                        most_played['normal']['avg_hunt'] = i['averageHunts']
                        most_played['normal']['top3'] = i['top3']
                        most_played['normal']['top5'] = i['top5']
                        most_played['normal']['top7'] = i['top7']
                        most_played['normal']['character_statistics'] = []
                        for j in range(len(i['characterStats'])):
                            most_played['normal']['character_statistics'].append(i['characterStats'][j])
                            most_played['normal']['character_statistics'][j]['characterCode'] = cha_code[most_played['normal']['character_statistics'][j]['characterCode']]
            # 최근 전적 20회
            recent_play = requests.get(URL+'games/'+userNum,headers=header).json()
            recent_match = []
            # 전적 검색 실패
            if recent_play['code'] != 200:
                return JsonResponse({'success':0})
            
            cnt = -1
            for i in range(len(recent_play['userGames'])):
                if recent_play['userGames'][i]['matchingTeamMode'] != int(team_mode):
                    continue
                recent_match.append({})
                cnt += 1
                recent_match[cnt]['date'] = recent_play['userGames'][i]['startDtm']
                recent_match[cnt]['chr_name'] = cha_code[recent_play['userGames'][i]['characterNum']]
                recent_match[cnt]['chr_img'] = 'https://raw.githubusercontent.com/sungguenja/lumiaimg/master/소형/'+recent_match[cnt]['chr_name']+'.png'
                recent_match[cnt]['level'] = recent_play['userGames'][i]['characterLevel']
                recent_match[cnt]['rank'] = recent_play['userGames'][i]['gameRank']
                recent_match[cnt]['kill_cnt'] = recent_play['userGames'][i]['playerKill']
                recent_match[cnt]['animal_cnt'] = recent_play['userGames'][i]['monsterKill']
                recent_match[cnt]['mastery'] = {}
                for index,(key,value) in enumerate(recent_play['userGames'][i]['masteryLevel'].items()):
                    recent_match[cnt]['mastery'][mastery_code[int(key)]] = value
                recent_match[cnt]['skill_pick'] = []
                for index,(key,value) in enumerate(recent_play['userGames'][i]['skillOrderInfo'].items()):
                    if value//1000000 != 1:
                        button = '무기스킬'
                    else:
                        button = value%1000
                        button = button//100
                        if button == 1:
                            button = '패시브'
                        elif button == 2:
                            button = 'Q'
                        elif button == 3:
                            button = 'W'
                        elif button == 4:
                            button = 'E'
                        else:
                            button = 'R'
                    recent_match[cnt]['skill_pick'].append(button)
                if recent_play['userGames'][i]['equipment'].get('0') != None:
                    recent_match[cnt]['weapon'] = item_code[recent_play['userGames'][i]['equipment']['0']]
                    recent_match[cnt]['weapon_img'] = 'https://raw.githubusercontent.com/sungguenja/lumiaimg/master/아이템/' + mastery_code[recent_play['userGames'][i]['bestWeapon']] + '/' + item_code[recent_play['userGames'][i]['equipment']['0']] + '.png'
                else:
                    recent_match[cnt]['weapon'] = None
                    recent_match[cnt]['weapon_img'] = None
                if recent_play['userGames'][i]['equipment'].get('1') != None:
                    recent_match[cnt]['head'] = item_code[recent_play['userGames'][i]['equipment']['1']]
                    recent_match[cnt]['head_img'] = 'https://raw.githubusercontent.com/sungguenja/lumiaimg/master/아이템/옷/' + item_code[recent_play['userGames'][i]['equipment']['1']] + '.png'
                else:
                    recent_match[cnt]['head'] = None
                    recent_match[cnt]['head_img'] = None
                if recent_play['userGames'][i]['equipment'].get('2') != None:
                    recent_match[cnt]['cloth'] = item_code[recent_play['userGames'][i]['equipment']['2']]
                    recent_match[cnt]['cloth_img'] = 'https://raw.githubusercontent.com/sungguenja/lumiaimg/master/아이템/머리/' + item_code[recent_play['userGames'][i]['equipment']['2']] + '.png'
                else:
                    recent_match[cnt]['cloth'] = None
                    recent_match[cnt]['cloth_img'] = None
                if recent_play['userGames'][i]['equipment'].get('3') != None:
                    recent_match[cnt]['arm'] = item_code[recent_play['userGames'][i]['equipment']['3']]
                    recent_match[cnt]['arm_img'] = 'https://raw.githubusercontent.com/sungguenja/lumiaimg/master/아이템/팔/' + item_code[recent_play['userGames'][i]['equipment']['3']] + '.png'
                else:
                    recent_match[cnt]['arm'] = None
                    recent_match[cnt]['arm_img'] = None
                if recent_play['userGames'][i]['equipment'].get('4') != None:
                    recent_match[cnt]['leg'] = item_code[recent_play['userGames'][i]['equipment']['4']]
                    recent_match[cnt]['leg_img'] = 'https://raw.githubusercontent.com/sungguenja/lumiaimg/master/아이템/다리/' + item_code[recent_play['userGames'][i]['equipment']['4']] + '.png'
                else:
                    recent_match[cnt]['leg'] = None
                    recent_match[cnt]['leg_img'] = None
                if recent_play['userGames'][i]['equipment'].get('5') != None:
                    recent_match[cnt]['accessory'] = item_code[recent_play['userGames'][i]['equipment']['5']]
                    recent_match[cnt]['accessory_img'] = 'https://raw.githubusercontent.com/sungguenja/lumiaimg/master/아이템/장식/' + item_code[recent_play['userGames'][i]['equipment']['5']] + '.png'
                else:
                    recent_match[cnt]['accessory'] = None
                    recent_match[cnt]['accessory_img'] = None
            return JsonResponse({'success':1,'most_played':most_played,'recent_match':recent_match},safe=False,json_dumps_params={'ensure_ascii': False})
        except json.decoder.JSONDecodeError:
            return JsonResponse({'success':0})
    else:
        return JsonResponse({'굳이 이렇게 오시나요':request.method})
    
def steam(request,news_cnt):
    response = requests.get('https://api.steampowered.com/ISteamNews/GetNewsForApp/v2?appid=1049590&count={0}'.format(news_cnt)).json()
    response = response['appnews']['newsitems']
    answer = {'response':[]}
    for i in range(len(response)):
        now = {}
        now['title'] = response[i]['title']
        now['click'] = response[i]['url']
        if '[img]' in response[i]['contents']:
            start = response[i]['contents'].index('[img]')+4
            end = response[i]['contents'].index('[/img]')
            text = response[i]['contents'][start:end]
            for j in range(len(text)):
                if text[j] == '/':
                    text = text[j:end]
                    break
            now['url'] = 'https://steamcdn-a.akamaihd.net/steamcommunity/public/images/clans' + text
        else:
            now['url'] = 'https://raw.githubusercontent.com/sungguenja/lumiaimg/master/loading1.png'
        answer['response'].append(now)
    return JsonResponse(answer)

def rank(request,mode):
    BSER_KEY = settings.BSER_KEY
    output = requests.get('https://open-api.bser.io/v1/rank/top/1/'+str(mode),headers={"accept":"application/json","x-api-key":BSER_KEY})
    return JsonResponse(output.json())