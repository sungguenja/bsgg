from django.urls import path
from . import views

app_name = 'matchhistory'
urlpatterns = [
    path('search/<str:user_name>/<str:season>/<str:team_mode>',views.searchhistory,name='searchhistory'),
    path('steam/<int:news_cnt>',views.steam,name='steam'),
    path('rank/<int:mode>',views.rank,name='rank')
]