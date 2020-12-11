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
    return JsonResponse(characters,safe=False,json_dumps_params={'ensure_ascii': False})