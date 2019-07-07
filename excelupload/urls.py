from django.conf.urls import include, url
from django.contrib import admin
from views import home,getExcel
urlpatterns = [
    url(r'^upload/', home),
    url(r'^getExcel/', getExcel)
]
