from django.shortcuts import render
from .models import *

# Create your views here.
def all_check(request):
    play_throughs = Playthrough.objects.all()
    play_throughs = serializers.serialize('json',play_throughs)
    play_throughs = json.loads(play_throughs)
    data = []
    for article in play_throughs:
        data.append({'pk':article['pk'],'title':article['fields']['title']})
    return JsonResponse(data,safe=False,json_dumps_params={'ensure_ascii': False})