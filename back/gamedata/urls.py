from django.urls import path
from . import views

app_name = 'gamedata'
urlpatterns = [
    path('',views.all_item,name='all_item'),
    path('search/<str:item_name>',views.search_item,name='search_item'),
    path('category/<int:category_type>',views.search_category,name='search_category'),
    path('detail/<int:pk>',views.item_detail,name='item_detail'),
    path('only/<int:pk>',views.only_that,name='only_that'),
    path('area/<int:pk>',views.all_area,name='all_area'),
    path('animal/<int:pk>',views.animal_detail,name='animal_detail'),
]