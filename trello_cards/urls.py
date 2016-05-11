from django.conf.urls import patterns, url
from trello_cards import views

urlpatterns = patterns('', url(r'^$', views.home, name='home'), )
