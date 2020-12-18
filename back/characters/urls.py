from django.urls import path
from . import views

app_name = 'characters'
urlpatterns = [
    path('',views.all_chr,name='all_chr'),
    path('detail/<int:pk>',views.detail,name='detail'),
    path('weapon/<int:pk>', views.detail_weapon,name='detail_weapon'),
]