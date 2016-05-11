import requests
import json


class List:
    def __init__(self, name, cards):
        self._name = name
        self._cards = cards

    # properties
    @property
    def cards(self):
        return self._cards

    @cards.setter
    def cards(self, value):
        self._cards = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    # end properties

    def __unicode__(self):
        return self._name


class Card:
    def __init__(self, name, link):
        self._name = name
        self._link = link

    # properties
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, value):
        self._link = value
    # end properties

    def __unicode__(self):
        return self._name + ":" + self._link


class APIParser:
    def __init__(self):
        self._lists = self._createLists()

    # properties
    @property
    def lists(self):
        return self._lists

    @lists.setter
    def lists(self, value):
        self._lists = value
    # end properties

    def _buildRequest(self):
        base = "https://api.trello.com/1/boards/4d5ea62fd76aa1136000000c/lists"
        key = "03ad10898a383e33747fb956330d0b5c"
        query_parms = {'key': key,
                       'cards': 'open',
                       'card_fields': 'name,url',
                       'fields': 'name'}
        return requests.get(base, params=query_parms)

    def _createLists(self):
        parsedJson = self._buildRequest().json()
        lists = []
        for list in parsedJson:
            trelloList = self._createList(list)
            lists.append(trelloList)
        return lists

    def _createList(self, list):
        name = list["name"]
        cards = list["cards"]
        cardsInList = []
        for card in cards:
            trelloCard = self._createCard(card)
            cardsInList.append(trelloCard)
        return List(name, cardsInList)

    def _createCard(self, cardJson):
        name = cardJson["name"]
        link = cardJson["url"]
        return Card(name, link)
