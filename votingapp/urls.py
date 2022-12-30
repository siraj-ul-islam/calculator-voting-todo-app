from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getquery', views.getquery, name='getquery'),
    path('sortdatavalueasc', views.sortdatavalueasc, name='sortdatavalueasc'),
    path('sortdatavaluedec', views.sortdatavaluedec, name='sortdatavaluedec'),
    path('sortdatakeyasc', views.sortdatakeyasc, name='sortdatakeyasc'),
    path('sortdatakeydec', views.sortdatakeydec, name='sortdatakeydec'),


]
