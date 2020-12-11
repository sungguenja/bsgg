from django.urls import path
from . import views

app_name = 'characters'
urlpatterns = [
    path('',views.all_chr,name='all_chr'),

]