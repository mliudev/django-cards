from django.shortcuts import render_to_response
from django.http import HttpResponse
from trello_cards.utils import APIParser


# Create your views here.
def home(request):
    parser = APIParser()
    trello_lists = parser.lists
    return render_to_response('home.html', {'trello_lists': trello_lists})
