from django.urls import path
from . import views

app_name = 'community'
urlpatterns = [
    path('',views.all_check,name='all_check'),
    path('gamedata/<int:pk>',views.gamedata,name='gamedata'),
]