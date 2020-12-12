from django.urls import path
from . import views

app_name = 'gamedata'
urlpatterns = [
    path('',views.datamine)
]