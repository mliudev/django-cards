from django.shortcuts import render
from django.http import HttpResponse
from trello_cards.utils import APIParser


# Create your views here.
def home(request):
    parser = APIParser()
    trello_lists = parser.lists
    return render(request, 'home.html', context={'trello_lists': trello_lists})
