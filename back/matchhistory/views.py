from django.http import JsonResponse
import requests, json
# Create your views here.
def searchhistory(request,user_name,season,team_mode):
    if request.method == 'GET':
        URL = 'http://matchhistory.playeternalreturn.com/'
        data = {'user_name':user_name,'season':season,'team_mode':team_mode}
        output = requests.post(URL+'statsKR_'+season,data=data).json()
        output = output['result']['output']
        return JsonResponse({'output':output},safe=False,json_dumps_params={'ensure_ascii': False})
    else:
        return JsonResponse({'굳이 이렇게 오시나요':request.method})