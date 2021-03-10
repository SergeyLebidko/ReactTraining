from django.urls import path
from .views import index, palette, dynamic_table, msg_list, preloader, popover, menu, slider_1, slider_2, animation, \
    search_component, toggle, buttons, table_component, paper_demo_1

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('palette/', palette, name='palette'),
    path('dynamic_table/', dynamic_table, name='dynamic_table'),
    path('msg_list/', msg_list, name='msg_list'),
    path('preloader/', preloader, name='preloader'),
    path('popover/', popover, name='popover'),
    path('menu/', menu, name='menu'),
    path('slider_1/', slider_1, name='slider_1'),
    path('slider_2/', slider_2, name='slider_2'),
    path('animation/', animation, name='animation'),
    path('search_component/', search_component, name='search_component'),
    path('toggle/', toggle, name='toggle'),
    path('buttons/', buttons, name='buttons'),
    path('table_component/', table_component, name='table_component'),
    path('paper_demo_1/', paper_demo_1, name='paper_demo_1')
]
