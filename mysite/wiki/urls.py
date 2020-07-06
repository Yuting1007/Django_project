from django.urls import path
from . import views

app_name = 'wiki'
urlpatterns = [
    path('', views.wiki_home, name='wiki_host'),
]
