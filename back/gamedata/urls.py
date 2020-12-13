from django.urls import path
from . import views

app_name = 'gamedata'
urlpatterns = [
    path('',views.all_item,name='all_item'),
    path('search/<str:item_name>',views.search_item,name='search_item'),
]